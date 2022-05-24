from tools import csv_to_dict, load_json, dump_json

#lista_municipios_regiao = csv_to_registros("regioes-saude.csv")
 
 

municipios = csv_to_dict("input/populacao.csv", "IBGE")

regioes = csv_to_dict("input/regioes-saude.csv", "CODIBGE")

array_geometria = load_json("input/boundaries-simplified.json")["features"]

dict_geometria = {str(objeto["properties"]["id"]): objeto["geometry"] for objeto in array_geometria }


completa_ibge = {}

dicionario_cidades = {}

for key, val in municipios.items():
    ibgend = key[:6]
    completa_ibge[int(ibgend)] = int(key)
    regiao = regioes[ibgend]["REGIAO"]
    dicionario_cidades[int(key)] = {"nome": val["Município"].replace(" (SC)", ""),
    "regiao": regiao, "geometria": dict_geometria[ibgend]} 

dump_json(dicionario_cidades, "output/dbcidades.json", ensure_ascii=False, indent=1)
dump_json(completa_ibge, "output/ibge.json", indent=1)