from django.conf.urls import url
from core.views import obterconfiguracao, atualizarlocalizacao

urlpatterns = [
   url(r'^core/obterconfiguracao$', obterconfiguracao),
   url(r'^core/atualizarlocalizacao', atualizarlocalizacao),
]
