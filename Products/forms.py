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