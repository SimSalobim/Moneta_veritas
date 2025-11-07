from django.shortcuts import render
from catalog.models import Coin, Banknote

# Create your views here.
def index(request):
    template = 'homepage/index.html'
    coin_list = Coin.objects.values(
        'id', 'name', 'category', 'denomination', 'description'
    ).filter(
        is_published=True,
        is_on_main=True,
    )
    banknote_list = Banknote.objects.values(
        'id', 'name', 'category', 'denomination', 'description'
    ).filter(
        is_published=True,
        is_on_main=True,
    )
    
    context = {
        'coin_list': coin_list,
        'banknote_list': banknote_list
    }
    return render(request, template, context)