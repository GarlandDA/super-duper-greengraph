
import geopy
import numpy
import yaml
import os
from unittest.mock import Mock
from unittest.mock import patch
import unittest.mock as mock
from greengraph.graph import Greengraph
from nose.tools import assert_equal, assert_almost_equal

os.chdir('C:\\Users\\Diego\\Documents\\greengraph\\greengraph\\test')

def test_Greengraph():
    g = Greengraph('place 1','place 2')
    assert_equal(g.start,'place 1')
    assert_equal(g.end,'place 2')
    assert_equal(g.geocoder.domain, 'maps.google.co.uk')
    
def test_geolocate():
    g = Greengraph('','')
    with mock.patch.object(g.geocoder, 'geocode') as mock_geocode:
        london_location = g.geolocate('London')
        mock_geocode.assert_called_with('London', exactly_one=False)

def test_location_sequence():
    with open(os.path.join(os.path.dirname(__file__),
                          'fixtures','loc_seqs.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            answer = fixture.pop('answer')
            g = Greengraph('','')
            numpy.testing.assert_array_equal(g.location_sequence(**fixture), answer)