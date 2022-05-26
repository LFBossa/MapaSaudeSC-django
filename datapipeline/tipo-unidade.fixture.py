import csv
from tools import tratatexto, csv_to_registros, dump_json


tipos = csv_to_registros('input/tipo_unidade.csv')

print(tipos)

tipos_fixture = [{
    "model": "mapa.TipoEstabelecimento",
    "pk": int(x["cod"]),
    "fields": { 
        "nome": tratatexto(x["tipo_unidade"])
    }
} for x in tipos]  

dump_json(tipos_fixture, 'fixtures/tipos.json', ensure_ascii=False, indent=1)