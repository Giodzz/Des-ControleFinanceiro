from django.urls import path
from . import views

app_name = "descontrole"

urlpatterns = [
    # localhost/descontrole/categorias
    path('categorias/', views.categorias, name='categorias')
]