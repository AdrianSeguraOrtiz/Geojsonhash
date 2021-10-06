import pygeohash as pgh
from operator import itemgetter

def get_geojson_id(geojson: dict) -> str:
    # TODO: Validate geojson
    representative_points = []
    polygon_ids = []
    features = geojson["features"]

    for element in features:
        geometry = element["geometry"]

        if geometry["type"] == "Polygon":
            points = geometry["coordinates"][0]
            points.pop()
            first_point = min(points,key=itemgetter(0,1))
            representative_points.append(first_point)
            first_point_index = points.index(first_point)
            ordered_points = points[first_point_index:] + points[:first_point_index]

            points_ids = []
            for p in ordered_points:
                point_id = pgh.encode(p[0], p[1], precision = 9)
                points_ids.append(point_id)
            polygon_id = "-".join(points_ids)
            polygon_ids.append(polygon_id)

    new_order = [representative_points.index(x) for x in sorted(representative_points,key=itemgetter(0,1))]
    ordered_polygon_ids = [polygon_ids[i] for i in new_order]

    geojson_id="--".join(ordered_polygon_ids)

    return geojson_id