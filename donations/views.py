from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
    
