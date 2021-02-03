from django.db import models
from django.urls import reverse

# Create your models here.

class ClassProducts(models.Model):
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=50)
    product_price = models.CharField(max_length=50)
    product_bool = models.BooleanField(default=True)
    
    def __str__(self):
        return self.product_name
    
    
