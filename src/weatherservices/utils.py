from noaa.utils import get_noaa_data
from weatherdotcom.utils import get_weatherdotcom_data
from accuweather.utils import get_accuweather_data


acceptable_filters = ['noaa', 'weather.com', 'accuweather']
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


def get_services_data(services_list, lat, lng):
    services_temp_list = []

    for service in services_list:
        services_temp_list.append(services_dict[service](lat, lng))

    return temps_average(services_temp_list)
