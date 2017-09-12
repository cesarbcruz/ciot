from django.contrib import admin

from .models import Configuracao, Localizacao

class ConfiguracaoAdmin(admin.ModelAdmin):
      list_display = ('pk', 'latitude', 'longitude', 'habilitado')

admin.site.register(Configuracao, ConfiguracaoAdmin)


class LocalizacaoAdmin(admin.ModelAdmin):
      list_display = ('pk', 'latitude', 'longitude', 'endereco', 'distancia', 'tempo_de_carro', 'datahora')

admin.site.register(Localizacao, LocalizacaoAdmin)
