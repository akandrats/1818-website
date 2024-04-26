from django.shortcuts import render
from .models import Product
from django.http import HttpResponse


def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'index2.html', {'product': product})


def home(request):
    return render(request, 'home.html')

