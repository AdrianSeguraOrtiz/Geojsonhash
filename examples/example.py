from geojsonhash import get_geojson_id
import json

with open("./resources/geojson.json") as geo_d:
    geojson = json.load(geo_d)

geojson_id = get_geojson_id(geojson)
print(geojson_id)