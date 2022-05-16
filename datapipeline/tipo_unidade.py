import csv


def tratatexto(texto: str) -> str:
    texto_array = texto.title().strip().split(" ")
    array_processado = [x.lower() if  len(x) < 3 else x for x in texto_array ]  
    return " ".join(array_processado)


with open('tipo_unidade.csv') as fp:
    reader = csv.DictReader(fp)
    for row in reader:
        print(f'({row["cod"]} , \"{tratatexto(row["tipo_unidade"])}\"),')
