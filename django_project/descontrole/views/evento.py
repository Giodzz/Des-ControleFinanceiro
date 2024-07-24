from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from ..forms.evento import EventoForm
from ..models.evento import Evento
from django.contrib import messages
from django.http import JsonResponse


def evento_index(request):
    form = EventoForm()
    eventos = Evento.objects.all()
    return render(
        request, "descontrole/evento/index.html", {"form": form, "eventos": eventos}
    )


def evento_create(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento salvo.")
            return JsonResponse({"success": "Evento salvo."}, status=201)
        
        else:
            messages.error(request, "Não foi possível criar evento.")
            return JsonResponse(
                {"error": "Não foi possível criar a evento."}, status=400
            )
    
# TODO
def evento_update(request):
    pass

#TODO
def evento_delete(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == "POST":
        evento.delete()
        messages.success(request, "Categoria deletada com sucesso.")
        if request.is_ajax():
            return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)

#TODO
def evento_export(request):
    pass