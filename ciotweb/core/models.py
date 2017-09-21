# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class Configuracao(models.Model):
  google_maps_api_key = models.CharField(verbose_name=u"Chave (API Maps)",
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


def user_directory_path(instance, filename):
    return 'usuario_{0}/{1}'.format(instance.usuario.id, filename)

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User,  unique=True, verbose_name=u"Usuário", help_text="Usuário")
    foto = models.ImageField(verbose_name=u"Foto", help_text="Foto do usuário", upload_to=user_directory_path)

    class Meta:
      verbose_name_plural = "Perfil dos usuários"

    def save(self):
        im = Image.open(self.foto)
        output = BytesIO()
        im = im.resize((60, 60))
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        self.foto = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.foto.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)
        super(PerfilUsuario, self).save()


