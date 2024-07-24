# Generated by Django 3.2.25 on 2024-07-22 16:11

import descontrole.models.enum
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('descontrole', '0026_auto_20240715_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimativa',
            name='natureza',
            field=models.CharField(choices=[('saida', 'Saida'), ('entrada', 'Entrada'), (descontrole.models.enum.NaturezaEnum.Meta, 'Meta')], max_length=7),
        ),
        migrations.AlterField(
            model_name='evento',
            name='natureza',
            field=models.CharField(choices=[('saida', 'Saida'), ('entrada', 'Entrada'), (descontrole.models.enum.NaturezaEnum.Meta, 'Meta')], max_length=7),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tipo',
            field=models.CharField(choices=[('pix', 'Pix'), ('debito', 'Debito'), ('credito', 'Credito'), ('dinheiro', 'Dinheiro'), ('boleto', 'Boleto'), ('outros', 'Outros'), (descontrole.models.enum.TipoEnum.Meta, 'Meta')], max_length=8),
        ),
    ]