from django.shortcuts import render
from django.views.generic import TemplateView

def menu_page(request):
    return render(request, 'menu.html')

def main_page(request):
    return render(request, 'main_page.html')


def shop_page(request):
    sukhmes = ['Клей для теплоизоляции', 'Клей для кладки', 'Клей для плитки', 'Штукатурка']

    context = {
        'sukhmes': sukhmes

    }
    return render(request, 'shop_page.html', context)

def bin_page(request):
    cont = 'Продолжить покупки'
    done = 'Оформить заказ'
    context = {
        'cont': cont,
        'done': done,

    }
    return render(request, 'bin_page.html', context)
    # Create your views here.
