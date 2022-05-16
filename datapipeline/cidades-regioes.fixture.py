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

regioes_fixtures = [{
    "model": "mapa.Regiao",
    "pk": x,
    "fields": {"nome": x} 
} for x in unique_regiao]

dump_json(municipios_fixtures, "fixtures/municipios.json", ensure_ascii=False, indent=1)
dump_json(regioes_fixtures, "fixtures/regioes.json", ensure_ascii=False, indent=1)

