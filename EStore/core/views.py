from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, "core/home.html", {})

def product_list(request):
    parts = Product.objects.all()
    return render(request, 'core/product_list.html', {'parts': parts})

def aboutus(request):
    return render(request, 'core/AboutUs.html')

def contact(request):
    return render(request, 'core/Contact.html')

def checkout(request):
    return render(request, 'core/checkout.html')