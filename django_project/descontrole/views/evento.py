from django.shortcuts import render, get_object_or_404, redirect
from ..forms.evento import EventoForm
from ..models.evento import Evento

def evento_index(request):
    form = EventoForm()
    eventos = Evento.objects.all()
    return render(request, "descontrole/evento/index.html", {"form": form, "eventos": eventos})
