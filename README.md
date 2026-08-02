# Milwaukee, Wisconsin Milwaukee Metropolitan Sewerage District Parser

Parses MMSD current statuses, including Deep Tunnel and water treatment plant capacities

### Installation

`python3 -m venv .venv`

`source .venv/bin/activate`

`pip3 install .`

### Run

`python mke_mmsd_parser.py`

```
MMSDInformation(facilities=[MMSDFacility(name='Deep Tunnel', current_million_gallons=348, maximum_million_gallons=432), MMSDFacility(name='South Shore Water Reclamation Facility', current_million_gallons=103, maximum_million_gallons=150), MMSDFacility(name='Jones Island Water Reclamation Facility', current_million_gallons=327, maximum_million_gallons=330)], water_drop_alert=False)
```

### Publishing

Get API key from [PyPI](https://pypi.org/)

`source .venv/bin/activate`

`python3 -m pip install --upgrade build twine`

`python3 -m build`

`python3 -m twine upload dist/*`, using your API key

