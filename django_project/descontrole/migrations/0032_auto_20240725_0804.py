# Generated by Django 3.2.25 on 2024-07-25 11:04

import descontrole.models.enum
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('descontrole', '0031_merge_0030_auto_20240723_2256_0030_auto_20240724_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimativa',
            name='natureza',
            field=models.CharField(choices=[('saida', 'Saida'), ('entrada', 'Entrada'), (descontrole.models.enum.NaturezaEnum.Meta, 'Meta')], max_length=7),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data',
            field=models.DateField(),
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