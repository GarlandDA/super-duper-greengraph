
import geopy
import numpy
import yaml
import os
from greengraph.map import Map
from unittest.mock import Mock
from unittest.mock import patch
import unittest.mock as mock
from greengraph.graph import Greengraph
from nose.tools import assert_equal, assert_almost_equal

def test_Map():
    mock_image = open(os.path.join(os.path.dirname(__file__),
                                   'fixtures','london_fixture.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        test_map = Map(51.5073509, -0.1277583)
        mock_get.assert_called_with(
            'http://maps.googleapis.com/maps/api/staticmap?',
            params=dict(size='400x400', zoom=10, center='51.5073509,-0.1277583',
                        style='feature:all|element:labels|visibility:off', sensor='false', maptype='satellite')
        )