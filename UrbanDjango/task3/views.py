from django.shortcuts import render
from django.views.generic import TemplateView

def main_page(request):
    return render(request, 'main_page.html')


def shop_page(request):
    facade = 'Клей для теплоизоляции'
    masonry = 'Клей для кладки'
    tile = 'Клей для плитки'
    plaster = 'Штукатурка'
    context = {
        'facade': facade,
        'masonry': masonry,
        'tile': tile,
        'plaster': plaster
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
