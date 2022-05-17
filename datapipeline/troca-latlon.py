import string
from tools import csv_to_dict, load_json, dump_json

array_boundaries = load_json("input/boundaries-simplified.json")

#  features : [
#      type: string,
#      geometry: {
#          type: string
#          coordinates: [[ [x,y] ]]     
#     }
#      properties
#  ]

for x in array_boundaries["features"]:
    novas_coordenadas = [ [b,a] for (a,b) in x["geometry"]["coordinates"][0]]
    x["geometry"]["coordinates"][0] = novas_coordenadas

dump_json(array_boundaries, "output/contornos-simplificados.json")
    