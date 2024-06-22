from django.shortcuts import render, get_object_or_404, redirect
from ..models import Categoria
from ..forms import CategoriaForm


def categoria_index(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "categoria_index"
            ) 
    else:
        form = CategoriaForm()

    categorias = Categoria.objects.all()
    return render(
        request,
        "descontrole/categoria/index.html",
        {"form": form, "categorias": categorias},
    )


def categoria_lista(request):
    categorias = Categoria.objects.all()
    return render(
        request,
        "descontrole/categoria/lista.html",
        {"categorias": categorias},
    )


def categoria_detalhes(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(
        request,
        "descontrole/categoria/detalhes.html",
        {"categoria": categoria},
    )


def categoria_create(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            return redirect("categoria_detalhes", pk=categoria.pk)
    else:
        form = CategoriaForm()
    return render(request, "descontrole/categoria/form.html", {"form": form})


def categoria_update(request, pk):
    categoria = get_object_or_404(categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save()
            return redirect("detalhes", pk=categoria.pk)
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, "descontrole/categoria/form.html", {"form": form})


def categoria_delete(request, pk):
    categoria = get_object_or_404(categoria, pk=pk)
    if request.method == "POST":
        categoria.delete()
        return redirect("lista")
    return render(
        request,
        "descontrole/categoria/confirm_delete.html",
        {"categoria": categoria},
    )
