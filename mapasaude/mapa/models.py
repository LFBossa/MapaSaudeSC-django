from django.db import models
from djgeojson.fields import PointField


class Estabelecimento(models.Model):
    nome = models.CharField(max_length=200)
    cnes = models.IntegerField(primary_key=True)
    endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE)
    TIPOS_ESTABELECIMENTO = [(1, "Posto de Saude"),
                             (2, "Centro de Saude/Unidade Basica"),
                             (4, "Policlinica"),
                             (5, "Hospital Geral"),
                             (7, "Hospital Especializado"),
                             (15, "Unidade Mista"),
                             (20, "Pronto Socorro Geral"),
                             (21, "Pronto Socorro Especializado"),
                             (22, "Consultorio Isolado"),
                             (32, "Unidade Movel Fluvial"),
                             (36, "Clinica/Centro de Especialidade"),
                             (39, "Unidade de Apoio Diagnóstico e Terapia (Sadt Isolado)"),
                             (40, "Unidade Movel Terrestre"),
                             (42, "Unidade Movel de Nivel Pre-Hospitalar na Area de Urgencia"),
                             (43, "Farmacia"),
                             (50, "Unidade de Vigilancia em Saude"),
                             (60, "Cooperativa ou Empresa de Cessao de Trabalhadores na Saude"),
                             (62, "Hospital/Dia - Isolado"),
                             (67, "Laboratorio Central de Saude Publica Lacen"),
                             (68, "Central de Gestao em Saude"),
                             (69, "Centro de Atencao Hemoterapia e ou Hematologica"),
                             (70, "Centro de Atencao Psicossocial"),
                             (71, "Centro de Apoio a Saude da Familia"),
                             (72, "Unidade de Atencao a Saude Indigena"),
                             (73, "Pronto Atendimento"),
                             (74, "Polo Academia da Saude"),
                             (75, "Telessaude"),
                             (76, "Central de Regulacao Medica Das Urgencias"),
                             (77, "Servico de Atencao Domiciliar Isolado (Home Care)"),
                             (78, "Unidade de Atencao em Regime Residencial"),
                             (79, "Oficina Ortopedica"),
                             (80, "Laboratorio de Saude Publica"),
                             (81, "Central de Regulacao do Acesso"),
                             (82, "Central de Notificacao,Captacao e Distrib de Orgaos Estadual"),
                             (83, "Polo de Prevencao de Doencas e Agravos e Promocao da Saude"),
                             (84, "Central de Abastecimento"),
                             (85, "Centro de Imunizacao"),
                             ]
    tipo = models.IntegerField(choices=TIPOS_ESTABELECIMENTO)

    def __str__(self):
        return self.nome + f" (CNES {self.cnes})"
# Create your models here.


class Endereco(models.Model):
    logradouro = models.CharField(max_length=250)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    municipio = models.ForeignKey("Municipio")
    localizacao = PointField()

    def __str__(self) -> str:
        return f"{self.logradouro}, {self.numero} | {self.bairro}"


class Municipio(models.Model):
    ibge = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=256)
    regiao = models.ForeignKey("Regiao")

    def __str__(self) -> str:
        return self.nome


class Regiao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome
