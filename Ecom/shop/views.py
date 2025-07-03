from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.

def index(request):
    categories = Product.objects.values_list('category', flat=True).distinct()
    allprods = []
    for category in categories:
        products = Product.objects.filter(category=category)[:4]  # Limit to 4 per category
        allprods.append((products, category))
    return render(request, 'shop/index.html', {'allprods': allprods})

def product_detail(request, product_id):
    product = Product.objects.filter(id=product_id)
    return render(request, 'shop/product.html', {'product': product[0]})

def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return render(request,'shop/test.html')
def search(request):
    return HttpResponse("search page")
def track(request):
    return HttpResponse("track order page")
def checkout(request):
    return HttpResponse("checkoutpage")