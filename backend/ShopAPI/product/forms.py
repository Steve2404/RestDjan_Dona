from django import forms
from .views import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'content', 'price')