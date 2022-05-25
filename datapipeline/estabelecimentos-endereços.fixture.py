from tools import csv_to_dict, load_json, dump_json

#lista_municipios_regiao = csv_to_registros("regioes-saude.csv")
 
 

CNES = csv_to_dict("input/estabelecimentos-top.csv", "CNES")

ibge = load_json("output/ibge.json")


# Estabelecimento
#     nome: string
#     cnes: numero PK
#     endereco: cnes
#     tipo: numero 

#  Endereco  
#     cnes: numero PK
#     logradouro: string
#     numero: int
#     bairro: string
#     cep: string
#     municipio: ibge
#     localizacao = PointField()

def num_or_zero(string: str)-> int:
    try: 
        return int(string)
    except:
        return 0

estabelecimento_fixture = [{
    "model": "mapa.Estabelecimento",
    "pk": int(key),
    "fields": {
        "nome": valor["NOME FANTASIA"],  
        "tipo": int(valor["TP_UNID"]),
        "municipio": ibge[ valor["IBGE"] ], # corrige o DV do IBGE
        "logradouro": valor["logradouro"],
        "numero": num_or_zero(valor["NUMERO"]),
        "bairro": valor["BAIRRO"], 
        "cep": valor["CEP"], 
        "localizacao": {'type': 'Point', 'coordinates': [float(valor["lon"]),float(valor["lat"])]}
        } }
    for key, valor in CNES.items()]

 

dump_json(estabelecimento_fixture, "fixtures/estabelecimentos.json", ensure_ascii=False, indent=1) 