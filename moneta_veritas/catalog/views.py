from django.shortcuts import render
from catalog.models import Coin, Banknote

# Create your views here.
def catalog_list(request):
    template = 'catalog/list.html'
    coin_list = Coin.objects.filter(is_published=True)
    banknote_list = Banknote.objects.filter(is_published=True)
    
    context = {
        'coin_list': coin_list,
        'banknote_list': banknote_list
    }
    return render(request, template, context)

def catalog_detail(request, pk):
    template = 'catalog/detail.html'
    coin = Coin.objects.filter(is_published=True, pk=pk).first()
    if coin:
        context = {'coin': coin}
        return render(request, template, context)
    
    # Если монета не найдена, ищем банкноту
    banknote = Banknote.objects.filter(is_published=True, pk=pk).first()
    if banknote:
        context = {'banknote': banknote}
        return render(request, template, context)
    
    # Если ничего не найдено - 404
    from django.http import Http404
    raise Http404("Объект не найден")