from django.contrib import admin

# Register your models here.
from .models import Product , Contact , User

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(User)