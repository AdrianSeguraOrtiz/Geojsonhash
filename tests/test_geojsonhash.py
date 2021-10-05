from pathlib import Path
from geojsonhash.geojsonhash import get_geojson_id
import json
import pytest


@pytest.mark.parametrize("geojson_file, id", [
    (Path("./tests/resources/geojson_1.json"), "v0qjzpfxg-vr93cxgpb-v7tggpgxu"),
    (Path("./tests/resources/geojson_2.json"), "s1r5yzcpu-sm86n0181-sdsccpgzf--vpypfrfzg-vpcryrvxg-vrcxypvzy-vxcrgrzxz"),
    (Path("./tests/resources/geojson_3.json"), "j0h04810j-j0j002p2n-j258n0425--jvb6184b1-jxe1gpupg-meqpzxcpv-mcfvfrgxf--vhxebxyzv-vpvpbrzry-vruxzxvrz-vxcryrcrz-vrz3zzuru"),
])
def test_check_geojson(geojson_file, id):
    with open(geojson_file) as geo_d:
        geojson = json.load(geo_d)
    assert get_geojson_id(geojson) == id
