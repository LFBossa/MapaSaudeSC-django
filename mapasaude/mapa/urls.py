from django.urls import path

from . import views

app_name = 'mapa'

urlpatterns = [
    path('cidades/', views.indexcidade, name='listacidades' ), 
    path('cidade/<int:pk>', views.cidadedetalhe, name='detalhecidade'),
    path('estado/', views.estado, name='estado' ), 
    path('api/estabelecimentos/cidade/<int:pk>', views.EstabelecimentoCidadeAPI, name="estabelecimentocidade"),
    path('api/estabelecimentos/tipo/<int:tipo>', views.EstabelecimentoTipoAPI, name="estabelecimentotipo"),
    path('api/estabelecimentos/tipo/', views.TiposEstabelecimentosAPI, name="tipos"),
    path('api/cidades/nomes/', views.ListaCidadesAPI, name='listacidadesapi')
    #path('regioes')
]