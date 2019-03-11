from urllib import request, parse

class Netspeak:
    _base_query_url = "http://api.netspeak.org/netspeak3/search"


    def __call__(self, user_input):
        query = self._encode_query(user_input)
        response = self._make_request(query)
        return self._read_result(response)

    def _encode_query(self, query):
        params = {"query" : query, "format": "text"}
        return parse.urlencode(params)

    def _make_request(self, query):
        url = self._base_query_url+"?"+query
        return request.urlopen(url)

    def _read_result(self, response):
        binary_data = response.read()
        data = binary_data.decode()
        return data






