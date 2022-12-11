import os
from django.contrib.gis.utils import LayerMapping
from .models import Swamp

swamp_mapping = {
    'cat': 'cat',
    'f_codedesc': 'F_CODEDESC',
    'f_code': 'F_CODE',
    'areakm2': 'AREAKM2',
    'geom': 'MULTIPOLYGON',
}

swp_shp = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'data/swamp.shp'))


def run(verbose=True):
    lm = LayerMapping(Swamp, swp_shp, swamp_mapping, transform=False,
                      encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
