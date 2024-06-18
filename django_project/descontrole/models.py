from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator


NATUREZA = (('saida', 'Saída'), 
            ('entrada', 'Entrada'))

TIPO = (('pix', 'PIX'), 
        ('debito', 'Cartão de débito'), 
        ('credito', 'Cartão de crédito'), 
        ('dinheiro', 'Dinheiro'), 
        ('boleto', 'Boleto'),
        ('outros', 'Outros'))


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, blank=False, unique=True)
    descricao = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.nome


class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=150, blank=True)
    data = models.DateField(blank=False)
    valor = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)], blank=False)
    natureza = models.CharField(max_length=7, choices=NATUREZA, blank=False)
    tipo = models.CharField(max_length=8, choices=TIPO, blank=False)

    def __str__(self):
        return str(self.id)


class Estimativa(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=150, blank=True)
    mes = models.PositiveIntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(12)])
    ano = models.PositiveIntegerField(blank=False, validators=[MaxValueValidator(datetime.now().year)])
    valor = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)], blank=False)
    natureza = models.CharField(max_length=7, choices=NATUREZA, blank=False)

    def __str__(self):
        return str(self.id)

