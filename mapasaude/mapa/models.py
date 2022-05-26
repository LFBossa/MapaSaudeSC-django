from django.db import models
from djgeojson.fields import PointField, PolygonField

import re

class TipoEstabelecimento(models.Model):
    n = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=200)
    municipio = models.ForeignKey("Municipio",on_delete=models.DO_NOTHING)
    cnes = models.IntegerField(primary_key=True) 
    tipo = models.ForeignKey("TipoEstabelecimento", on_delete=models.DO_NOTHING)
    logradouro = models.CharField(max_length=250)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    localizacao = PointField()

    @property
    def llcoord(self):
        lon, lat = self.localizacao['coordinates']
        return [lat, lon]

    @property
    def endereco(self):
        strn = "" if self.numero == 0 else f", {self.numero}"
        return f"{self.logradouro}{strn} - {self.bairro}\n{self.municipio.nome}"

    @property
    def tipo_unidade(self):
        return self.tipo.nome


    def __str__(self):
        return self.nome + f" (CNES {self.cnes})"
# Create your models here.

 


class Municipio(models.Model):
    ibge = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=256)
    regiao = models.ForeignKey("Regiao",on_delete=models.DO_NOTHING)
    geometria = PolygonField()
    
    @property
    def cor(self):
        return self.regiao.cor

    def __str__(self) -> str:
        return self.nome


class Regiao(models.Model):
    def valida_cor(cor: str):
        if not re.match("#[0-9A-F]{6}", cor):
            raise ValueError("Cor precisa ser no formato hexadeximal RGB.")
    
    nome = models.CharField(max_length=100, primary_key=True)
    cor = models.CharField(max_length=7, validators=[valida_cor])
    
    def __str__(self) -> str:
        return self.nome
