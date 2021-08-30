from django import forms




class NewsForm(forms.Form):
    news_time = forms.CharField(max_length=20)
    news_text = forms.CharField(max_length=100)
    news_inform = forms.CharField(max_length=100)
    