from django.urls import path

from . import views

app_name = 'mapa'

urlpatterns = [
    path('cidades', views.indexcidade, name='listacidades' ), 
    path('cidade/<int:pk>', views.DetalheCidade.as_view(), name='detalhecidade'),
    path('estado', views.estado, name='estado' ), 
    #path('regioes')
]