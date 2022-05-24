from tools import load_json, csv_to_dict

logradouros = load_json("input/logradouros.json")

estabelecimentos = csv_to_dict("input")

print(logradouros['9144439'])

