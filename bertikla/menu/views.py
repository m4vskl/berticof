from django.shortcuts import render
from .models import Products, Categories

def menu_list(request):
    products = Products.objects.filter(is_active=True)
    categories = Categories.objects.all().order_by('order')
    return render(request, 'menu_list.html', {'products': products, 'categories': categories})