from io import BytesIO
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from ..forms.evento import EventoForm
from ..models.evento import Evento
from django.contrib import messages
from django.http import JsonResponse
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter
import pandas as pd


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
            messages.error(request, "Não foi possível criar o evento.")
            return JsonResponse(
                {"error": "Não foi possível criar o evento."}, status=400
            )


def evento_update(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento atualizado com sucesso.")
            return JsonResponse(
                {"success": "Evento atualizado com sucesso."}, status=200
            )
        else:
            messages.error(request, "Não foi possível salvar o Evento.")
            return JsonResponse(
                {"error": "Não foi possível salvar o Evento."}, status=400
            )


def evento_delete(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == "POST":
        evento.delete()
        messages.success(request, "Evento deletado com sucesso.")
        if request.is_ajax():
            return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)


def evento_export(request):
    queryset = Evento.objects.all()
    df = pd.DataFrame(list(queryset.values()))
    if df.empty:
        return JsonResponse(
            {"error_message": "Nenhum item disponível para exportar."}, status=400
        )

    categorias = (
        Evento.objects.select_related("categoria_id")
        .values_list("categoria_id__id", "categoria_id__nome")
        .distinct()
    )
    df["categoria_id"] = df["categoria_id"].replace(dict(categorias))
    df = df.rename(columns={"categoria_id": "categoria"})
    df = df.drop(columns=["id"])
    df["data"] = df["data"].astype("datetime64[ns]").dt.strftime("%d/%m/%Y")
    df.columns = df.columns.str.capitalize()
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="mymodel_data.pdf"'
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    data = [df.columns.tolist()] + df.values.tolist()
    table = Table(data)
    style = TableStyle(
        [
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.Color(153 / 255.0, 204 / 255.0, 102 / 255.0),
            ),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Courier-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
        ]
    )
    table.setStyle(style)
    elements.append(table)
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
