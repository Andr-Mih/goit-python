from django.db import models

class Record(models.Model):
    record_type = models.CharField(max_length=20)

    def __str__(self):
        return self.record_type

class Category(models.Model):
    category_text_1 = models.CharField(max_length=20)
    #type_date = models.DateTimeField('type date')
    

    def __str__(self):
        return self.category_text


class Credit(models.Model):
    credit_value = models.CharField(max_length=20)
    category_text = models.CharField(max_length=20)
    record_type = models.CharField(max_length=20)
    credit_date = models.DateTimeField(null=True, blank=True)
    #value_type = models.ForeignKey(Record, on_delete=models.CASCADE)
    #credit_type = models.ForeignKey(Category, on_delete=models.CASCADE)





