from django.conf.urls import url
from core.views import obterconfiguracao, atualizarlocalizacao, HomeView, ConfiguracaoView, ControleView

urlpatterns = [
   url(r'^core/obterconfiguracao$', obterconfiguracao),
   url(r'^core/atualizarlocalizacao', atualizarlocalizacao),
   url(r'^$', HomeView.as_view(), name='home'),
   url(r'^controle$', ControleView.as_view(), name='controle'),
   url(r'^configuracao$', ConfiguracaoView.as_view(), name='configuracao'),
]
