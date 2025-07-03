from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    image = models.ImageField(upload_to='shop/images', default="")
    product_name=models.CharField(max_length=50)
    prodect_desc=models.CharField(max_length=300)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    pubs_date=models.DateField()
    
    def __str__(self):
        return self.product_name