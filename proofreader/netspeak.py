#!/bin/env python

from urllib import parse, request


NETSPEAK_REST_BASE_URL = "http://api.netspeak.org/netspeak3/search"


class Netspeak:
    _base_query_url = NETSPEAK_REST_BASE_URL
    
    def __call__(self, user_input):
        query = self._encode_query(user_input)
        url = self._make_request(query)
        return self._read_result(url)
        
    def _encode_query(self, query):
        params = {"query": query, "format": "text"}
        return parse.urlencode(params)

    def _make_request(self, query):
        return request.urlopen(self._base_query_url+"?"+query)

    def _read_result(self, url):
        return url.read().decode()
    
