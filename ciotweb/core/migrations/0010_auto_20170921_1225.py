# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_perfilusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='foto',
            field=models.ImageField(default='media/user.jpg', help_text='Foto do usuário', upload_to='media/', verbose_name='Foto'),
        ),
    ]
