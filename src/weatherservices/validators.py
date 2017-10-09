from rest_framework.validators import ValidationError

from weatherservices.utils import acceptable_filters
from common.googlemaps import gmaps


def filters_validator(filters):
    filters_error = ValidationError({
        'detail': 'Invalid filters input.',
        'description': 'Filters must be list containing one of {}, {}, {}'.format(*acceptable_filters)
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
            'detail': 'Invalid filters input.',
            'description': 'Filters must be list containing one of {}, {}, {}'.format(*acceptable_filters)
        })
