from django.contrib import admin
from .models import Categories, Products
from .models import *




class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_id', 'price')
    search_fields = ('name', 'price')

admin.site.register(Categories)
admin.site.register(Products, ProductAdmin)