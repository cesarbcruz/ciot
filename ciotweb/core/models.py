# -*- coding: utf-8 -*-
from django.db import models

class Configuracao(models.Model):
  google_distancematrix_api_key = models.CharField(verbose_name=u"Chave (DistanceMatrix)", help_text="Chave da api google distancematrix", max_length=255)
  google_maps_api_key = models.CharField(verbose_name=u"Chave (Maps)",
                                                   help_text="Chave da api google maps", max_length=255)
  latitude = models.CharField(verbose_name=u"Latitude", help_text="Latitude do endereço da sua casa", max_length=255)
  longitude  = models.CharField(verbose_name=u"Longitude", help_text="Longitude do endereço da sua casa", max_length=255)
  habilitado = models.BooleanField(verbose_name=u"Habilitado", help_text="Habilita ou desabilita a configuração", default=False)
  class Meta:
    verbose_name_plural = "Configurações"

class Localizacao(models.Model):
  latitude = models.CharField(verbose_name=u"Latitude", help_text="Latitude da última localização", max_length=255)
  longitude = models.CharField(verbose_name=u"Longitude", help_text="Longitude da última localização", max_length=255)
  endereco = models.CharField(verbose_name=u"Endereço", help_text="Endereço da última localização", max_length=255)
  distancia = models.CharField(verbose_name=u"Distância", help_text="Distância da sua casa (KM)", max_length=255)
  tempo_de_carro = models.CharField(verbose_name=u"Tempo de carro", help_text="Tempo de carro até sua casa (Minutos)", max_length=255)
  datahora = models.DateTimeField(verbose_name=u"Data/Hora", help_text="Data e Hora da última localização", auto_now=True, editable=False, null=False, blank=False)
  class Meta:
    verbose_name_plural = "Localizações"