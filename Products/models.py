from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.TextField()
    product_desc = models.TextField()
    product_price = models.TextField()
    product_bool = models.BooleanField(default=True)
    
    def __str__(self):
        return self.product_name