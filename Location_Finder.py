import json
import urllib.response


def get_location():
    resp = urllib.request.urlopen("http://ip-api.com/json")
    ip_address = json.load(resp)
    location_country = ip_address['country']
    location_city = ip_address['region']
    return location_country + " " + location_city
