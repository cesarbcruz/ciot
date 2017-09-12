from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

from django.views.generic import TemplateView

from core.models import Configuracao, Localizacao

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


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        localizacao = localizacao = Localizacao.objects.all().first()
        context['google_maps_api_key'] = localizacao.google_maps_api_key
        if localizacao:
            context['origem'] = "{0}, {1}".format(localizacao.latitude, localizacao.longitude)
        configuracao = Configuracao.objects.all().first()
        if configuracao:
            context['destino'] = "{0}, {1}".format(configuracao.latitude, configuracao.longitude)
        return context