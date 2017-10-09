from googlemaps.exceptions import HTTPError

from noaa.utils import get_noaa_data
from weatherdotcom.utils import get_weatherdotcom_data
from accuweather.utils import get_accuweather_data
from common.googlemaps import gmaps
from weatherservices.validators import (
    acceptable_filters,
    filters_validator,
    number_validator,
    lat_lng_validator,
    input_validator,
    zip_code_error
)

services_dict = {
    'noaa': get_noaa_data,
    'weather.com': get_weatherdotcom_data,
    'accuweather': get_accuweather_data
}


def temps_average(temps_list):
    taverage = {
        'f': 0,
        'c': 0
    }

    for tdict in temps_list:
        taverage['f'] += tdict['fahrenheit']
        taverage['c'] += tdict['celsius']

    return {
        'fahrenheit': taverage['f'] / len(temps_list),
        'celsius': taverage['c'] / len(temps_list)
    }


def validate_input_get_data(user_input):
    input_validator(user_input)

    lat = None
    lng = None

    if 'lat' and 'lng' in user_input:
        lat = user_input['lat']
        lng = user_input['lng']
    else:
        lat_lng = zipcode_to_lat_lng(user_input['zip_code'])
        lat, lng = lat_lng['lat'], lat_lng['lng']

    filters = user_input['filters']

    filters_validator(filters)
    number_validator('lat', lat)
    number_validator('lng', lng)
    lat_lng_validator(lat, lng)

    return get_services_data(filters, lat, lng)


def zipcode_to_lat_lng(zip_code):
    try:
        lat_lng = gmaps.geocode(zip_code)
    except HTTPError:
        raise zip_code_error

    if not lat_lng:
        raise zip_code_error

    return lat_lng[0]['geometry']['location']


def get_services_data(services_list, lat, lng):
    services_temp_list = []

    for service in services_list:
        services_temp_list.append(services_dict[service](lat, lng))

    return temps_average(services_temp_list)
