from django import forms

from .models import ClassProducts

class ClassProductForm(forms.ModelForm):
    class Meta:
        model = ClassProducts
        fields = [
            "product_name",
            "product_desc",
            "product_price"
        ]


class RawProductForm(forms.Form):
    product_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        "placeholder": "Product Name"
    }))
    product_desc = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        "placeholder": "Description"
    }))
    product_price = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        "placeholder": "Price"
    }))