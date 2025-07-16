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

def Signup(request):
    if request.method=="POST":
        try:
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            phone = request.POST.get('phone','')
            password = request.POST.get('password','')
            role = request.POST.get('role','Student')
            
            # Basic validation
            if not name or not email or not password:
                messages.error(request, 'Please fill in all required fields.')
                return render(request, 'shop/signup.html')
            
            # Check if user already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'A user with this email already exists.')
                return render(request, 'shop/signup.html')
            
            # Create new user
            user = User(
                name=name,
                email=email,
                phone=phone if phone else "0",  # Handle empty phone
                password=password,
                role=role
            )
            user.save()
            
            # Log user in automatically after signup
            request.session['user_id'] = user.user_id
            
            messages.success(request, f'Account created successfully! Welcome {name}!')
            return redirect('shop:index')  # Redirect to home page after successful signup
            
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return render(request, 'shop/signup.html')
    
    return render(request,'shop/signup.html')

def search(request):
    return HttpResponse("search page")

def track(request):
    return HttpResponse("track order page")

def checkout(request):
    return HttpResponse("checkoutpage")

def login(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email, password=password)
            # Store user in session
            request.session['user_id'] = user.user_id
            messages.success(request, f'Welcome back, {user.name}!')
            return redirect('shop:index')
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
    
    return render(request,'shop/login.html')

def logout(request):
    # Clear user session
    request.session.pop('user_id', None)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('shop:index')

def account(request):
    # Get current user from session
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, 'Please login to access your account.')
        return redirect('shop:login')
    
    try:
        current_user = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        request.session.pop('user_id', None)
        messages.error(request, 'User not found. Please login again.')
        return redirect('shop:login')
    
    return render(request,'shop/account.html', {'user': current_user})