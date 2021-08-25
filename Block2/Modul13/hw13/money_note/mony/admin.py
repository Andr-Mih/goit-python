from django.contrib import admin

# Register your models here.
from .models import Record, Credit, Category
from .forms import CreditForm



admin.site.register(Record)
admin.site.register(Category)
admin.site.register(Credit)
