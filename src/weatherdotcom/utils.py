from requests import post

from common.utils import normalize_temps


def get_weatherdotcom_data(lat, lng):
    url = 'http://127.0.0.1:5000/weatherdotcom'
    # url = 'http://172.17.0.1:5000/weatherdotcom'
    payload = {'lat': lat, 'lon': lng}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"
    }
    data = post(url, json=payload, headers=headers).json()
    raw_temp = data['query']['results']['channel']['condition']['temp']
    raw_temp_units = data['query']['results']['channel']['units']['temperature']

    return normalize_temps(
        raw_temp if raw_temp_units == 'F' else False,
        raw_temp if raw_temp_units == 'C' else False
    )
