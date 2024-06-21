from django.http import HttpResponse
from django.shortcuts import render
from .models import Categoria


def categorias(request):
    if request.POST.get('nome'):
        nova_categoria = Categoria()
        nova_categoria.nome = request.POST.get('nome')
        nova_categoria.descricao = request.POST.get('descricao')
        nova_categoria.save()

    categorias = {
        'categorias': Categoria.objects.all()
    }
    
    return render(request, "descontrole/categorias/index.html", categorias)
