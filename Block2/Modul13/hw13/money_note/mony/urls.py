from django.urls import path

from . import views

app_name = 'mony'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.record_add, name='add'),
    path('comfirm/', views.comfirm_record, name='comfirm'),
    #path('', views.detail, name='detail'),
]

#path('<int:question_id>/', views.detail, name = 'detail'),