from django.urls import path, re_path
from .views import categoria_create
from django.views.generic import TemplateView, RedirectView
from . import views

# app_name = "descontrole"

urlpatterns = [
    re_path(r"^$", RedirectView.as_view(url="home", permanent=False)),
    path("home", views.index, name="index"),
    path("categorias/", views.categoria_index, name="categoria_index"),
    path("categorias/export/", views.categoria_export, name="categoria_export"),
    path("categorias/create/", views.categoria_create, name="categoria_create"),
    path(
        "categorias/update/<int:pk>/", views.categoria_update, name="categoria_update"
    ),
    path(
        "categorias/delete/<int:pk>/", views.categoria_delete, name="categoria_delete"
    ),
    path("eventos/", views.evento_index, name="evento_index"),
    path("eventos/create/", views.evento_create, name="evento_create"),
    path("eventos/update/<int:pk>", views.evento_update, name="evento_update"),
    path("eventos/delete/<int:pk>", views.evento_delete, name="evento_delete"),
    path("eventos/export", views.evento_export, name="evento_export"),
    path("consulta/", views.consulta_index, name="consulta_index"),
]
