from django import forms
from .models import Product

class searchForm(forms.Form):
    name = forms.CharField(label='Entry a name', max_length = 200, required=False)
    code = forms.CharField(label='Entry a code', max_length = 200, required=False)


    
class addForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'code')   