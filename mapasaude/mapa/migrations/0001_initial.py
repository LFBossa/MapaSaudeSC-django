# Generated by Django 4.0.4 on 2022-05-16 19:39

from django.db import migrations, models
import django.db.models.deletion
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('cnes', models.IntegerField(primary_key=True, serialize=False)),
                ('logradouro', models.CharField(max_length=250)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=8)),
                ('localizacao', djgeojson.fields.PointField()),
            ],
        ),
        migrations.CreateModel(
            name='Regiao',
            fields=[
                ('nome', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('ibge', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=256)),
                ('geometria', djgeojson.fields.PolygonField()),
                ('regiao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mapa.regiao')),
            ],
        ),
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('nome', models.CharField(max_length=200)),
                ('cnes', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.IntegerField(choices=[(1, 'Posto de Saude'), (2, 'Centro de Saude/Unidade Basica'), (4, 'Policlinica'), (5, 'Hospital Geral'), (7, 'Hospital Especializado'), (15, 'Unidade Mista'), (20, 'Pronto Socorro Geral'), (21, 'Pronto Socorro Especializado'), (22, 'Consultorio Isolado'), (32, 'Unidade Movel Fluvial'), (36, 'Clinica/Centro de Especialidade'), (39, 'Unidade de Apoio Diagnóstico e Terapia (Sadt Isolado)'), (40, 'Unidade Movel Terrestre'), (42, 'Unidade Movel de Nivel Pre-Hospitalar na Area de Urgencia'), (43, 'Farmacia'), (50, 'Unidade de Vigilancia em Saude'), (60, 'Cooperativa ou Empresa de Cessao de Trabalhadores na Saude'), (62, 'Hospital/Dia - Isolado'), (67, 'Laboratorio Central de Saude Publica Lacen'), (68, 'Central de Gestao em Saude'), (69, 'Centro de Atencao Hemoterapia e ou Hematologica'), (70, 'Centro de Atencao Psicossocial'), (71, 'Centro de Apoio a Saude da Familia'), (72, 'Unidade de Atencao a Saude Indigena'), (73, 'Pronto Atendimento'), (74, 'Polo Academia da Saude'), (75, 'Telessaude'), (76, 'Central de Regulacao Medica Das Urgencias'), (77, 'Servico de Atencao Domiciliar Isolado (Home Care)'), (78, 'Unidade de Atencao em Regime Residencial'), (79, 'Oficina Ortopedica'), (80, 'Laboratorio de Saude Publica'), (81, 'Central de Regulacao do Acesso'), (82, 'Central de Notificacao,Captacao e Distrib de Orgaos Estadual'), (83, 'Polo de Prevencao de Doencas e Agravos e Promocao da Saude'), (84, 'Central de Abastecimento'), (85, 'Centro de Imunizacao')])),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapa.endereco')),
            ],
        ),
        migrations.AddField(
            model_name='endereco',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mapa.municipio'),
        ),
    ]
