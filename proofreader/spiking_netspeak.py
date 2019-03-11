#!/bin/env python

from urllib import request, parse

base_url = "http://api.netspeak.org/netspeak3/search"

parms = {
    "query": "looking forward to * you",
    "format": "text",
}
querystring = parse.urlencode(parms)

u = request.urlopen(base_url+"?"+querystring)
resp = u.read()

print(resp.decode())


# input:  
"""La la la, hey <ns:looking forward to ? you> in the meeting"""

# output:
"""La la la, hey <ns[out]:looking forward to seeing you,> in the meeting"""
