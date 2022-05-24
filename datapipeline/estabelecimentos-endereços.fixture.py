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

estabelecimento_fixture = [{
    "model": "mapa.Estabelecimento",
    "pk": int(key),
    "fields": {
        "nome": valor["NOME FANTASIA"], 
        "endereco": int(key), 
        "tipo": int(valor["TP_UNID"]),
        "municipio": ibge[ valor["IBGE"] ], # corrige o DV do IBGE
        } }
    for key, valor in CNES.items()]

def num_or_zero(string: str)-> int:
    try: 
        return int(string)
    except:
        return 0

endereco_fixture = [{
    "model": "mapa.Endereco",
    "pk": int(key),
    "fields": {
        "logradouro": valor["logradouro"],
        "numero": num_or_zero(valor["NUMERO"]),
        "bairro": valor["BAIRRO"], 
        "cep": valor["CEP"],
        "municipio": ibge[ valor["IBGE"] ], # corrige o DV do IBGE
        "localizacao": {'type': 'Point', 'coordinates': [float(valor["lat"]), float(valor["lon"])]}
    }

} for key, valor in CNES.items()]


dump_json(estabelecimento_fixture, "fixtures/estabelecimentos.json", ensure_ascii=False, indent=1)
dump_json(endereco_fixture, "fixtures/endereços.json", ensure_ascii=False, indent=1)