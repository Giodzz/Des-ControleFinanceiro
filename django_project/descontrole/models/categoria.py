from django.db import models


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, blank=False, unique=True)
    descricao = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'descontrole'