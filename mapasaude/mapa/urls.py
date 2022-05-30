from django.urls import path

from djgeojson.views import GeoJSONLayerView
from mapa.models import Municipio

from . import views

app_name = 'mapa'

urlpatterns = [
    path('cidades/', views.indexcidade, name='listacidades' ), 
    path('cidade/<int:pk>', views.cidadedetalhe, name='detalhecidade'),
    path('estado/', views.estado, name='estado' ), 
    path('api/estado/', GeoJSONLayerView.as_view(model=Municipio, properties=("nome","ibge","regiao","cor",), geometry_field="geometria"),
    name='estadoapi' ),
    path('api/estabelecimentos/cidade/<int:pk>', views.EstabelecimentoCidadeAPI, name="estabelecimentocidade"),
    path('api/estabelecimentos/tipo/<int:tipo>', views.EstabelecimentoTipoAPI, name="estabelecimentotipo"),
    path('api/estabelecimentos/tipo/', views.TiposEstabelecimentosAPI, name="tipos"),
    path('api/cidades/nomes/', views.ListaCidadesAPI, name='listacidadesapi'),
    path('api/atendimentos/<int:doenca>/ano-<int:ano>', views.DoencaAnoAPI, name='doencaano'),
    path('api/atendimentos/<int:doenca>/cidade-<int:cidade>', views.DoencaCidadeAPI, name='doencacidade')
    #path('regioes')
]