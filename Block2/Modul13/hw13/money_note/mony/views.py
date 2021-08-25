from django.forms.widgets import DateTimeInput
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Credit, Record, Category
from .forms import CreditForm, CategoryForm
from django.template import loader


def index(request):
    record_list = Credit.objects.all()
    template = loader.get_template('mony/index.html')
    context = {
        'record_list': record_list
    }
    return HttpResponse(template.render(context, request))

def record_add(request):
    sub = request.POST.get('submit')
    credit_value = 0
    category_text = ''
    record_type = ''
    credit_date = ''
    
    form = CreditForm(request.POST or None)
    
    if form.is_valid():
        value= form.cleaned_data.get("credit_value")
        credit_date= form.cleaned_data.get("credit_date")
        category_text= form.cleaned_data.get("category_text")
        record_type = form.cleaned_data.get("record_type")

        forma = Credit(credit_value=value, record_type=record_type, category_text=category_text, credit_date=credit_date)

        forma.save()
    
    context= {'form': form, 'credit_value': credit_value,
              'sub': sub,
              'category_text':category_text, 
              'record_type': record_type}
    
    return render(request, 'mony/add.html', context)
   # return HttpResponse(template.render(context, request))





def comfirm_record(request):
    record_list = Credit.objects.all()
    template = loader.get_template('mony/comfirm.html')
    context = {
        'record_list': record_list
    }
    return HttpResponse(template.render(context, request))







