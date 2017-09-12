# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170912_0016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(help_text='Latitude da última localização', max_length=255, verbose_name='Latitude')),
                ('longitude', models.CharField(help_text='Longitude da última localização', max_length=255, verbose_name='Longitude')),
                ('endereco', models.CharField(help_text='Endereço da última localização', max_length=255, verbose_name='Endereço')),
                ('distancia', models.CharField(help_text='Distância da sua casa', max_length=255, verbose_name='Distância')),
                ('tempo_de_carro', models.CharField(help_text='Tempo de carro até sua casa', max_length=255, verbose_name='Tempo de carro')),
            ],
            options={
                'verbose_name_plural': 'Localizações',
            },
        ),
    ]
