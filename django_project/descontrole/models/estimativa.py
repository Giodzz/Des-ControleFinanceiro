from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from .enum import NaturezaEnum, TipoEnum
from .categoria import Categoria


class Estimativa(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=150, blank=True)
    mes = models.PositiveIntegerField(
        blank=False, validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    ano = models.PositiveIntegerField(
        blank=False, validators=[MaxValueValidator(datetime.now().year)]
    )
    valor = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0)], blank=False
    )
    natureza = models.CharField(
        max_length=7, choices=NaturezaEnum.choices(), blank=False
    )

    def __str__(self):
        return str(self.id)
    
    class Meta:
        app_label = 'descontrole'