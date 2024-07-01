from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from ..models import Categoria
from django.contrib import messages
from ..forms import CategoriaForm
from django.http import HttpResponse
from io import BytesIO
import pandas as pd
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter


def categoria_index(request):
    form = CategoriaForm()
    categorias = Categoria.objects.all()
    return render(
        request,
        "descontrole/categoria/index.html",
        {"form": form, "categorias": categorias},
    )


def categoria_create(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            return redirect("categoria_index")
    else:
        form = CategoriaForm()
    return render(request, "descontrole/categoria/form_invalido.html", {"form": form})


def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria atualizada com sucesso.")
            return redirect("categoria_index")
        else:
            messages.error(
                request,
                "Não foi possível salvar a categoria.",
            )
    return redirect("categoria_index")


def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        categoria.delete()
        messages.success(request, "Categoria deletada com sucesso.")
        if request.is_ajax():
            return JsonResponse({"success": True})
        return redirect("categoria_index")
    return JsonResponse({"success": False}, status=400)


def categoria_export(request):
    queryset = Categoria.objects.all()
    df = pd.DataFrame(list(queryset.values()))

    if df.empty:
        return JsonResponse(
            {"error_message": "Nenhum item disponível para exportar."}, status=400
        )

    df = df.drop(columns=["id"])
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
