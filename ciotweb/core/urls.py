from django.conf.urls import url
from core.views import obterconfiguracao, atualizarlocalizacao, IndexView

urlpatterns = [
   url(r'^core/obterconfiguracao$', obterconfiguracao),
   url(r'^core/atualizarlocalizacao', atualizarlocalizacao),
   url(r'^$', IndexView.as_view()),
]