# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_localizacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='localizacao',
            name='datahora',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='localizacao',
            name='distancia',
            field=models.CharField(help_text='Distância da sua casa (KM)', max_length=255, verbose_name='Distância'),
        ),
        migrations.AlterField(
            model_name='localizacao',
            name='tempo_de_carro',
            field=models.CharField(help_text='Tempo de carro até sua casa (Minutos)', max_length=255, verbose_name='Tempo de carro'),
        ),
    ]
