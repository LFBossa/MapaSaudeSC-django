import csv
import json


def csv_to_registros(path : str) -> list:
    with open(path) as fp:
        resultado = []
        reader = csv.DictReader(fp)
        cabecalho = reader.fieldnames
        for row in reader: 
            resultado.append({a: row[a] for a in cabecalho})
    return resultado 

def csv_to_dict(path : str, key: str ) -> dict:
    with open(path) as fp:
        resultado = {}
        reader = csv.DictReader(fp)
        cabecalho = reader.fieldnames.copy()
        cabecalho.remove(key)
        for row in reader: 
            resultado[row[key]] = {a: row[a] for a in cabecalho}
    return resultado
    
def load_json(path: str) -> dict:
    with open(path) as fp:
        jsondict = json.load(fp)
    return jsondict

def dump_json(object: dict, path: str, **kwargs):
    with open(path, "w") as fp:
        json.dump(object, fp, **kwargs)

if __name__ == "__main__":
    print(csv_to_dict("datapipeline/regioes-saude.csv", "CODIBGE"))