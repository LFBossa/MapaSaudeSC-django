from multiprocessing import context
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.core.serializers import serialize
from django.views.decorators.cache import cache_page
from django.db.models import Sum, Q
from .models import Estabelecimento, Municipio, TipoEstabelecimento, Doenca, RegistroAtendimento


class ListaCidade(generic.ListView):
    model = Municipio


class DetalheCidade(generic.DetailView):
    model = Municipio
    template_name = "mapas/municipio_detail.html"
    context_object_name = "cidade"


def indexcidade(request):
    context = {'lista_municipios': Municipio.objects.order_by(
        'nome'), 'letras': [chr(x) for x in range(65, 65+26)]}
    return render(request, 'mapas/listacidades.html', context)


def cidadedetalhe(request, pk):
    cidade = Municipio.objects.get(pk=pk)

    context = {'cidade': cidade, }
    return render(request, 'mapas/municipio_detail.html', context)


def estado(request):
    todosmunicipios = Municipio.objects.all()
    return render(request, 'mapas/estado.html', {'lista_municipios': todosmunicipios})
 
def informacoes_estabelecimento(estabelecimento):
    return {'coordenadas': estabelecimento.llcoord,
            'nome': estabelecimento.nome,
            'endereco': estabelecimento.endereco,
            'cnes': estabelecimento.cnes,
            'tipo': estabelecimento.tipo.nome}


@cache_page(24 * 60 * 60)
def EstabelecimentoCidadeAPI(request, pk):
    #cidade = Municipio.objects.get(pk=pk)
    estabeles = Estabelecimento.objects.filter(municipio=pk)
    resposta = [informacoes_estabelecimento(x) for x in estabeles]
    return JsonResponse(resposta, safe=False)


@cache_page(24 * 60 * 60)
def EstabelecimentoTipoAPI(request, tipo):
    #cidade = Municipio.objects.get(pk=pk)
    estabeles = Estabelecimento.objects.filter(tipo=tipo)
    resposta = [informacoes_estabelecimento(x) for x in estabeles]
    return JsonResponse(resposta, safe=False)


@cache_page(24 * 60 * 60)
def TiposEstabelecimentosAPI(request):
    tipos = [(x.n, x.nome) for x in TipoEstabelecimento.objects.all()]
    return JsonResponse(tipos, safe=False)


@cache_page(24 * 60 * 60)
def ListaCidadesAPI(request):
    lista_cidades = [{"ibge": x.ibge, "nome": x.nome,
                      "regiao": x.regiao.nome} for x in Municipio.objects.all()]
    return JsonResponse(lista_cidades, safe=False)


@cache_page(24 * 60 * 60)
def DoencaAnoAPI(request, doenca, ano):
    atdano = Sum('registroatendimento__atendimentos',
                 filter=Q(registroatendimento__doenca=doenca,
                          registroatendimento__referencia__year=ano))
    query = Municipio.objects.annotate(atendimentos=atdano)
    doenca = Doenca.objects.get(pk=doenca)
    resposta = {"doença": doenca.nome, "atendimentos": [(x.ibge,x.atendimentos) for x in query]}
    return JsonResponse(resposta, safe=False)

@cache_page(24 * 60 * 60)
def DoencaCidadeAPI(request, doenca, cidade):
    atendimentos = RegistroAtendimento.objects.filter(
        doenca=doenca, municipio=cidade)
    dd = Doenca.objects.get(pk=doenca)
    municipio = Municipio.objects.get(pk=cidade)
    registros = {"municipio": municipio.nome, "doença": dd.nome,
        "registros": [(x.referencia, x.atendimentos) for x in atendimentos ]
    }
    return JsonResponse(registros)
