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
    
class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    phone=models.CharField(default=0)
    message=models.CharField(max_length=500,default="")
    
    def __str__(self):
        return self.name
    
