from django.urls import path
from .views import categoria_create
from django.views.generic import TemplateView
from . import views

# app_name = "descontrole"

urlpatterns = [
    path("categorias/", views.categoria_index, name="categoria_index"),
    path("categorias/lista/", views.categoria_lista, name="categoria_lista"),
    path("categorias/<int:pk>/", views.categoria_detalhes, name="categoria_detalhes"),
    path("categorias/create/", views.categoria_create, name="categoria_create"),
    path(
        "categorias/update/<int:pk>/", views.categoria_update, name="categoria_update"
    ),
    path(
        "categorias/delete/<int:pk>/", views.categoria_delete, name="categoria_delete"
    ),
]
