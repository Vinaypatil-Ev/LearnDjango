from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.TextField()
    product_desc = models.TextField()
    product_price = models.TextField()
    
    def __str__(self):
        return self.product_name