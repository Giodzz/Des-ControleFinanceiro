from django.shortcuts import render, get_object_or_404, redirect
from ..forms.evento import EventoForm

def evento_index(request):
    form = EventoForm()
    return render(request, "descontrole/evento/index.html", {"form": form})
