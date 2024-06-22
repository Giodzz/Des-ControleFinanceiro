from django.shortcuts import render, get_object_or_404, redirect

def consulta_index(request):
    return render(request, "descontrole/consulta/index.html")