#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

from geocoder.base import OneResult, MultipleResultsQuery


class MapcatResult(OneResult):

    def __init__(self, json_content):
        super(MapcatResult, self).__init__(json_content)

    @property
    def lat(self):
        lat = self.raw['geometry']['position']['coordinates'][1]
        return float(lat)

    @property
    def lng(self):
        lng = self.raw['geometry']['position']['coordinates'][0]
        return float(lng)


class MapcatQuery(MultipleResultsQuery):

    provider = 'mapcat'
    method = 'geocode'

    _URL = 'https://api.mapcat.com/location/search'
    _RESULT_CLASS = MapcatResult
    _KEY_MANDATORY = True

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'query': location
        }

    def _build_headers(self, provider_key, **kwargs):
        return {
            'X-Api-Key': provider_key
        }

    def _parse_results(self, json_response):
        super()._parse_results(json_response['result']['results'])
