from django.shortcuts import render


def categorias(request):
    return render(request, "descontrole/categorias/index.html", {})