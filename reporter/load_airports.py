import os
from django.contrib.gis.utils import LayerMapping
from .models import Airport

airport_mapping = {
    'id': 'ID',
    'fk_region': 'fk_region',
    'elev': 'ELEV',
    'name': 'NAME',
    'use': 'USE',
    'geom': 'MULTIPOINT',
}

arp_shp = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'data/airports.shp'))


def run(verbose=True):
    lm = LayerMapping(Airport, arp_shp, airport_mapping, transform=False,
                      encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
