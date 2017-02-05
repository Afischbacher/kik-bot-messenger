import json
import urllib.request


def get_location():
    resp = urllib.request.urlopen("http://ip-api.com/json")
    ip_address = json.load(resp)
    location_country = ip_address['country']
    location_region = ip_address['region']
    return "Looks like I am in the country of {0} and the region of {1}".format(location_country,location_region)
