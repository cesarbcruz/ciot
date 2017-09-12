from django.contrib import admin

from .models import Configuracao

class ConfiguracaoAdmin(admin.ModelAdmin):
      list_display = ('pk', 'latitude', 'longitude', 'habilitado')

admin.site.register(Configuracao, ConfiguracaoAdmin)
