# -*- coding: utf-8 -*-
from django.db import models

class Configuracao(models.Model):
  google_distancematrix_api_key = models.CharField(verbose_name=u"Chave (DistanceMatrix)", help_text="Chave da api google distancematrix", max_length=255)
  latitude = models.CharField(verbose_name=u"Latitude", help_text="Latitude do endereço da sua casa", max_length=255)
  longitude  = models.CharField(verbose_name=u"Longitude", help_text="Longitude do endereço da sua casa", max_length=255)
  habilitado = models.BooleanField(verbose_name=u"Habilitado", help_text="Habilita ou desabilita a configuração", default=False)
  class Meta:
    verbose_name_plural = "Configurações"
