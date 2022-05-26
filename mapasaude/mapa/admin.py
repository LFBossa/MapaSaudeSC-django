from django.contrib import admin
from .models import Municipio, Regiao, Estabelecimento
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
admin.site.register(Municipio, LeafletGeoAdmin)

admin.site.register(Regiao)

admin.site.register(Estabelecimento, LeafletGeoAdmin) 