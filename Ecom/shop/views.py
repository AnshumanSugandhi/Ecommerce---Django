from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product , Contact , User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def index(request):
    categories = Product.objects.values_list('category', flat=True).distinct()
    allprods = []
    for category in categories:
        products = Product.objects.filter(category=category)[:4]  # Limit to 4 per category
        allprods.append((products, category))
    
    # Get current user from session
    user_id = request.session.get('user_id')
    current_user = None
    if user_id:
        try:
            current_user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            # Clear invalid session
            request.session.pop('user_id', None)
    
    return render(request, 'shop/index.html', {
        'allprods': allprods,
        'current_user': current_user
    })

def product_detail(request, product_id):
    product = Product.objects.filter(id=product_id)
    return render(request, 'shop/product.html', {'product': product[0]})

def about(request):
    # Get current user from session
    user_id = request.session.get('user_id')
    current_user = None
    if user_id:
        try:
            current_user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            request.session.pop('user_id', None)
    
    return render(request,'shop/about.html', {'current_user': current_user})

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        message=request.POST.get('message','')
        contact=Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')
    
    # Get current user from session
    user_id = request.session.get('user_id')
    current_user = None
    if user_id:
        try:
            current_user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            request.session.pop('user_id', None)
    
    return render(request,'shop/contact.html', {'current_user': current_user})


def search(request):
    return HttpResponse("search page")

def track(request):
    return HttpResponse("track order page")

def checkout(request):
    return HttpResponse("checkoutpage")

