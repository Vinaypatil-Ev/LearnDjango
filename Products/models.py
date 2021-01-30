from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField()
    product_desc = models.CharField()
    product_price = models.CharField()