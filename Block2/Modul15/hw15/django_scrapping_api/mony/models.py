from django.db import models




class News(models.Model):
    news_time = models.CharField(max_length=20)
    news_text = models.CharField(max_length=20)
    news_inform = models.CharField(max_length=20)
   
    
    



