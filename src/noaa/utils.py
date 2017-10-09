from requests import get

from common.utils import normalize_temps


def get_noaa_data(lat, lng):
    url = 'http://127.0.0.1:5000/noaa?latlon={},{}'.format(lat, lng)
    # url = 'http://172.17.0.1:5000/noaa?latlon={},{}'.format(lat, lng)
    data = get(url).json()
    raw_temp_dict = data['today']['current']

    return normalize_temps(
        raw_temp_dict['fahrenheit'] if 'fahrenheit' in raw_temp_dict else False,
        raw_temp_dict['celsius'] if 'celsius' in raw_temp_dict else False
    )
