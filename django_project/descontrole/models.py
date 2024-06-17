from django.db import models


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, blank=False)
    descricao = models.CharField(max_length=150)
