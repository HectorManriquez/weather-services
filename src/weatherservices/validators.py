from rest_framework.validators import ValidationError

from common.googlemaps import gmaps

acceptable_input = ['lat', 'lng', 'zip_code', 'filters']
acceptable_filters = ['noaa', 'weather.com', 'accuweather']

zip_code_error = ValidationError({
    'detail': 'Invalid zip code.',
    'description': 'A non valid zip code was entered.'
})


def input_validator(user_input):
    input_error = ValidationError({
        'detail': 'Invalid input.',
        'description': 'Input must contain {}, {}, {}, {}'.format(*acceptable_input)
    })

    if 'lat' not in user_input or 'lng' not in user_input:
        if 'zip_code' not in user_input:
            raise input_error

    for input_val in list(user_input):
        if input_val not in acceptable_input:
            raise input_error


def filters_validator(filters):
    filters_error = ValidationError({
        'detail': 'Invalid filters.',
        'description': 'Filters must be a list containing one of {}, {}, {}'.format(*acceptable_filters)
    })

    if not isinstance(filters, list) or not filters:
        raise filters_error

    for curr_filter in filters:
        if curr_filter not in acceptable_filters:
            raise filters_error


def number_validator(name, value):
    if not (isinstance(value, (float, int))):
        raise ValidationError({
            'detail': 'Invalid {}'.format(name),
            'description': '{} must be a valid number'.format(name)
        })


def lat_lng_validator(lat, lng):
    # valid lat 40.714224 lng -73.961452
    # invalid lat 10 lng -45.53
    validated = gmaps.reverse_geocode((lat, lng))

    if not validated:
        raise ValidationError({
            'detail': 'Invalid lat and lng.',
            'description': 'A non valid set of lat and lng was entered.'
        })
