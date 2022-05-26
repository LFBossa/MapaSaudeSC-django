from multiprocessing import context
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.core.serializers import serialize


from .models import Estabelecimento, Municipio


class ListaCidade(generic.ListView):
    model = Municipio

class DetalheCidade(generic.DetailView):
    model = Municipio
    template_name = "mapas/municipio_detail.html"
    context_object_name = "cidade"


def indexcidade(request):
    context = {'lista_municipios' : Municipio.objects.order_by('nome')}
    return render(request, 'mapas/listacidades.html', context)

def cidadedetalhe(request, pk):
    cidade = Municipio.objects.get(pk=pk) 
    context = {'cidade': cidade,  }
    return render(request, 'mapas/municipio_detail.html', context)

def estado(request):
    gejson = Municipio.objects.all() 
    return render(request, 'mapas/estado.html', {'lista_municipios': gejson} )

def EstabelecimentoCidadeAPI(request,pk):
    #cidade = Municipio.objects.get(pk=pk)
    estabeles = Estabelecimento.objects.filter(municipio=pk)
    resposta = [ {'coordenadas': x.llcoord(), 
                    'nome': x.nome, 
                    'endereco': x.endereco(), 
                    'cnes': x.cnes, 
                    'tipo': x.get_tipo_display()} for x in estabeles ]
    return JsonResponse(resposta, safe=False)


