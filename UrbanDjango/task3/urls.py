from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main_page, name='main_page'),
    path('shop/', views.shop_page, name='shop_page'),
    path('bin/', views.bin_page, name='bin_page'),
]