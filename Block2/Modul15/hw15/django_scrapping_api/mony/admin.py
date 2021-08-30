from django.contrib import admin

# Register your models here.
from .models import News
from .forms import NewsForm



#admin.site.register(Record)
#admin.site.register(Category)
admin.site.register(News)
