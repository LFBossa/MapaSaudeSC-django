from tools import csv_to_registros, load_json, dump_json
from pytz import timezone
from datetime import datetime

TZ = timezone("America/Sao_Paulo")


def ref2date(referencia: str):
    ano, mes = int(referencia[:4]), int(referencia[4:])
    # return TZ.localize(datetime(ano, mes, 1))
    return datetime(ano, mes, 1)


registros = csv_to_registros("input/saude-series.csv")

lista_doencas = list(registros[0].keys())[1:-3]
doencas_pre_dict = dict(enumerate(lista_doencas))
doencas_dict = {k+1: v for (k, v) in doencas_pre_dict.items()}
doenças_map = {v: k for (k, v) in doencas_dict.items()}

doenças_fixture = [
    {"model": "mapa.Doenca",
     "pk": k,
     "fields": {
         "nome": v
     }} for (k, v) in doencas_dict.items()]

ibge_table = load_json("output/ibge.json")

atendimentos_fixture = []

if __name__ == "__main__":
    for reg in registros:
        ibge = ibge_table[reg["Ibge"]]
        for nome, k in doenças_map.items():
            fixturezinha = {
                "model": "mapa.RegistroAtendimento",
                "pk": f"{ibge}-{reg['referencia']}-{k}",
                "fields": {
                    "doenca": k,
                    "municipio": ibge,
                    "referencia": ref2date(reg['referencia']).isoformat(),
                    "atendimentos": reg[nome]
                }

            }
            atendimentos_fixture.append(fixturezinha)

dump_json(doenças_fixture, "fixtures/doenças.json", ensure_ascii=False)
dump_json(atendimentos_fixture, "fixtures/atendimentos.json", ensure_ascii=False)