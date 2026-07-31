# Milwaukee, Wisconsin Milwaukee Metropolitan Sewerage District Parser

Gets the current status of the Deep Tunnels

### Installation

`python3 -m venv .venv`

`source .venv/bin/activate`

`pip3 install .`

### Run

`python mke_mmsd_parser.py`

```
[MMSDFacilityInformation(name='Deep Tunnel', current_million_gallons=8, maximum_million_gallons=432), MMSDFacilityInformation(name='South Shore Water Reclamation Facility', current_million_gallons=61, maximum_million_gallons=150), MMSDFacilityInformation(name='Jones Island Water Reclamation Facility', current_million_gallons=63, maximum_million_gallons=330)]
```

### Publishing

Get API key from [PyPI](https://pypi.org/)

`source .venv/bin/activate`

`pip3 install setuptools twine`

`python3 setup.py sdist`

`twine upload dist/*`, using your API key

