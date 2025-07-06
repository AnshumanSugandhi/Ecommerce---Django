from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product , Contact
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
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        message=request.POST.get('message','')
        contact=Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
    return render(request,'shop/contact.html')
def search(request):
    return HttpResponse("search page")
def track(request):
    return HttpResponse("track order page")
def checkout(request):
    return HttpResponse("checkoutpage")