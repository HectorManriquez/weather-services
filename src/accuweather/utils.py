from requests import get

from common.utils import normalize_temps


def get_accuweather_data(lat, lng):
    url = 'http://127.0.0.1:5000/accuweather?latitude={}&longitude={}'.format(lat, lng)
    # url = 'http://172.17.0.1:5000/accuweather?latitude={}&longitude={}'.format(lat, lng)
    data = get(url).json()
    raw_temp_dict = data['simpleforecast']['forecastday'][0]['current']

    return normalize_temps(
        raw_temp_dict['fahrenheit'] if 'fahrenheit' in raw_temp_dict else False,
        raw_temp_dict['celsius'] if 'celsius' in raw_temp_dict else False
    )
