from django.urls import path
from . import views

app_name = "descontrole"

urlpatterns = [
    path('categorias', views.categorias, name='categorias')
]