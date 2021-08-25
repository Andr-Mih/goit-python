from django import forms


class Record(forms.Form):
    record_type = forms.CharField(max_length=20)

    def __str__(self):
        return self.record_type

class CategoryForm(forms.Form):
    category_text_1 = forms.CharField(max_length=20)
    #type_date = models.DateTimeField('type date')
    

    def __str__(self):
        return self.category_text

class CreditForm(forms.Form):
    credit_value = forms.IntegerField()
    credit_date = forms.DateTimeField()
    record_type = forms.CharField(max_length=20)
    category_text = forms.CharField(max_length=20)
    