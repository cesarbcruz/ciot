from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from core.models import Configuracao

def obterconfiguracao(request):
    configuracao_as_json = serializers.serialize('json', Configuracao.objects.filter(habilitado=True))
    return HttpResponse(configuracao_as_json, content_type='json')
