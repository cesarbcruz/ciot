from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

from django.views.generic import TemplateView
from core import PrevisaoTempo as previsaoTempo
from core.models import Configuracao, Localizacao, PerfilUsuario


def obterconfiguracao(request):
    configuracao_as_json = serializers.serialize('json', Configuracao.objects.filter(habilitado=True))
    return HttpResponse(configuracao_as_json, content_type='json')

@csrf_exempt
def atualizarlocalizacao(request):
    if request.method == 'POST':
            data = json.loads(str(request.body, 'utf-8'))
            print('Latitude: {0}'.format(data['latitude']))
            print('Longitude: {0}'.format(data['longitude']))
            print('Endereço: {0}'.format(data['endereco']))
            print('Distância: {0} KM'.format(data['distancia'] / 1000))
            print('Tempo de carro: {0} minuto(s)'.format(data['tempo_de_carro'] / 60))
            localizacao = Localizacao.objects.all().first()
            if not localizacao:
                print('Nova localizacao')
                localizacao = Localizacao.objects.create()
            localizacao.latitude = data['latitude']
            localizacao.longitude = data['longitude']
            localizacao.endereco = data['endereco']
            localizacao.distancia = round(data['distancia']/1000, 2)
            localizacao.tempo_de_carro = round(data['tempo_de_carro']/60, 2)
            localizacao.save()

    return HttpResponse("OK")


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['opcao'] = 'home'

        if self.request.user.is_authenticated():
            perfil = PerfilUsuario.objects.filter(usuario=self.request.user)
            if perfil:
                context['perfilusuario'] = perfil[0]

        localizacao = localizacao = Localizacao.objects.all().first()
        if localizacao:
            context['origem'] = "{0}, {1}".format(localizacao.latitude, localizacao.longitude)
            previsaolocal = previsaoTempo.obter(localizacao.latitude, localizacao.longitude)
            context['temperaturalocal'] = str(round(previsaolocal['main']['temp'], 1))
            context['nebulosidadelocal'] = str(previsaolocal['clouds']['all']) + ' %'
            context['umidadelocal'] = str(previsaolocal['main']['humidity']) + ' %'
            context['cidadelocal'] = str(previsaolocal['name'])
            context['descricaotempolocal'] = str(previsaolocal['weather'][0]['description'])
            context['iconetempolocal'] = str(previsaolocal['weather'][0]['icon'])
            if float(localizacao.distancia) > 1:
                context['distanciacasa'] = localizacao.distancia
                context['tempodecarrocasa'] = localizacao.tempo_de_carro

        configuracao = Configuracao.objects.all().first()
        if configuracao:
            context['destino'] = "{0}, {1}".format(configuracao.latitude, configuracao.longitude)
            context['google_maps_api_key'] = configuracao.google_maps_api_key
            previsao = previsaoTempo.obter(configuracao.latitude, configuracao.longitude)
            context['temperaturacasa'] = str(round(previsao['main']['temp'], 1))
            context['nebulosidadecasa'] = str(previsao['clouds']['all']) + ' %'
            context['umidadecasa'] = str(previsao['main']['humidity']) + ' %'
            context['cidadecasa'] = str(previsao['name'])
            context['descricaotempocasa'] = str(previsao['weather'][0]['description'])
            context['iconetempocasa'] = str(previsao['weather'][0]['icon'])
        return context

class ControleView(TemplateView):
    template_name = "controle.html"

    def get_context_data(self, **kwargs):
        context = super(ControleView, self).get_context_data(**kwargs)
        context['opcao'] = 'controle'
        return context

class ConfiguracaoView(TemplateView):
    template_name = "configuracao.html"

    def get_context_data(self, **kwargs):
        context = super(ConfiguracaoView, self).get_context_data(**kwargs)
        context['opcao'] = 'configuracao'
        return context