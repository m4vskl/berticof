from django.shortcuts import render
from .models import Products, Categories

def menu_list(request):
    products = Products.objects.all()
    categories = Categories.objects.all()
    return render(request, 'menu_list.html', {'products': products, 'categories': categories})