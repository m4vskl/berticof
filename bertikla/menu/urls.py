from django.urls import path
from .views import menu_list
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', menu_list, name='menu_list'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
