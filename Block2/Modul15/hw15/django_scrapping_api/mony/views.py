from django.forms.widgets import DateTimeInput
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import News
from .forms import NewsForm
from django.template import loader
import requests
import re
from bs4 import BeautifulSoup

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .serializers import CreditSerializer
url = 'https://www.ukr.net/news/technologies.html'


def index(request):
    record_list = News.objects.all()
    template = loader.get_template('mony/index.html')
    context = {
        'record_list': record_list
    }
    return HttpResponse(template.render(context, request))

def record_add(request):
    sub = request.POST.get('submit')
    news_time = ''
    news_text = ''
    news_inform = ''
        
    form = NewsForm(request.POST or None)
    htm = requests.get(url)
    html = htm.text
    soup = BeautifulSoup(html, 'lxml')
    minimum = html.find('class_="im-tl_a"')
    inform = soup.find_all('div', class_='im-pr')[:9]
    time = soup.find_all('time', class_='im-tm')[:9]
    
    #minimum = html[:10]
    #inform = html[15:30]
    #time = html[45:90]
    for i in range(0,9):
        news_text = minimum[i]
        news_time = time[i]
        news_inform = inform[i]

        forma = News(news_text=news_text, news_time=news_time, news_inform=news_inform)
        forma.save()

       
    return render(request, 'mony/index.html')
   





def comfirm_record(request):
    record_list = News.objects.all()
    template = loader.get_template('mony/comfirm.html')
    context = {
        'record_list': record_list
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = News.objects.all()
        serializer = CreditSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CreditSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Credit.objects.get(pk=pk)
    except Credit.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CreditSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CreditSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)











