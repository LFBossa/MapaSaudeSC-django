from enum import unique
from textwrap import indent
from tools import load_json, dump_json


dbcidades = load_json("output/dbcidades.json")

municipios_fixtures = [{
    "model": "mapa.Municipio",
    "pk": int(key),
    "fields": valor
} for (key, valor) in dbcidades.items()]

regioes = [ x["regiao"] for x in dbcidades.values() ]

unique_regiao = list(set(regioes))
unique_regiao.sort() 

VERDINHO = "#76e598"
ROXO = "#8539bd"
SALMAO = "#ffa87d"
AZUL = "#4c67c2"
CINZA = "#c9c9c9"
VERDE = "#20a548"
ROSA = "#ff0066"

cores = [SALMAO, AZUL, SALMAO, VERDE, VERDINHO, VERDE,
ROSA, CINZA, VERDE, SALMAO, AZUL, ROXO, VERDINHO, ROXO, 
SALMAO, VERDINHO]

regioes_fixtures = [{
    "model": "mapa.Regiao",
    "pk": x,
    "fields": {"nome": x, "cor": cores[n] } 
} for (n,x) in enumerate(unique_regiao)]

dump_json(municipios_fixtures, "fixtures/municipios.json", ensure_ascii=False, indent=1)
dump_json(regioes_fixtures, "fixtures/regioes.json", ensure_ascii=False, indent=1)

