from django.urls import path
from .views import menu_list



urlpatterns = [
    path('', menu_list, name='menu_list'),
    ]