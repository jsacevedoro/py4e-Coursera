"""The program will prompt for a location, contact a web service and 
retrieve JSON for the web service and parse that data, 
and retrieve the first place_id from the JSON. 
A place ID is a textual identifier that uniquely identifies a place as within Google Maps."""

import urllib.request, urllib.parse
import json


# API Service URL
service_url = "http://py4e-data.dr-chuck.net/json?"

# Prompt user for the Location
address = input('Enter location: ')

# Create parameters for the request
parms = dict()
parms["address"] = address
parms["key"] = 42
# Create the request
url = service_url + urllib.parse.urlencode(parms)
# Send the request
url_handle = urllib.request.urlopen(url)
# Pull the data and turn into python string
data = url_handle.read().decode()

# Turn data into Dictionary
data = json.loads(data)
print(data["results"][0]["place_id"])