from django.shortcuts import render


def categorias_index(request):
    return render(request, "categorias/index.html", {})