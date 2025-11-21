from django.shortcuts import render


souvenirs = [
    {
        'id': 0,
        'title': 'Монета 1812 года',
        'description': 'Монета, найденная в лагере, оставленным Наполеоном.'
    },
    {
        'id': 1,
        'title': 'Игла Кащея',
        'description': 'Игла, предназначенная для отшивания чушпанов'
    },
]
# Create your views here.
def catalog_list(request):
    template = 'catalog/list.html'
    context = {'catalog_list': souvenirs}
    return render(request, template, context)


def catalog_detail(request, pk):
    template = 'catalog/detail.html'
    context = {'souvenir': souvenirs[pk]}
    return render(request, template, context)