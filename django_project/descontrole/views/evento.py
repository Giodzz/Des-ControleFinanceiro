from django.shortcuts import render, get_object_or_404, redirect


def evento_index(request):
    return render(request, "descontrole/evento/index.html")
