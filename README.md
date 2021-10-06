# geojsonhash

![CI](https://github.com/AdrianSeguraOrtiz/geojsonhash/actions/workflows/ci.yml/badge.svg)
![Release](https://github.com/AdrianSeguraOrtiz/geojsonhash/actions/workflows/release.yml/badge.svg)
![Pypi](https://img.shields.io/pypi/v/geojsonhash)
![License](https://img.shields.io/apm/l/geojsonhash)
<img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

This package is responsible for generating identifiers for geojson objects. To do so, it makes use of the pygeohash library in charge of generating the identifiers of the different points contained in the geojson.

In this implementation, individual points are ignored, treating the input geojson as a set of polygons defining a surface. The polygons are sorted according to their coordinates while the northwest-most vertex of the polygons defines the starting point for encoding. 

## Installation

To install the package there are two options: through poetry or by using the pip command

### Pip command

```bash
$ pip install geojsonhash
```

### Poetry

```bash
$ git clone https://github.com/AdrianSeguraOrtiz/geojsonhash.git
$ cd geojsonhash
$ poetry install
```

## Example

An example is shown below:

```python
from geojsonhash import get_geojson_id
import json

with open("./resources/geojson.json") as geo_d:
    geojson = json.load(geo_d)

geojson_id = get_geojson_id(geojson)
print(geojson_id)
```

To run it through console we can do:

```bash
$ cd examples
$ python example.py
```