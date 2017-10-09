from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from weatherservices.utils import get_services_data
from weatherservices.validators import filters_validator, number_validator


@api_view(['GET', 'POST'])
def average_temperature(request):
    if request.method == 'POST':
        data = request.data
        lat = data['lat']
        lng = data['lng']
        filters = data['filters']

        filters_validator(filters)
        number_validator('lat', lat)
        number_validator('lng', lng)

        accu = get_services_data(filters, lat, lng)
        # print(data)
        return Response(accu, content_type='application/json', status=status.HTTP_200_OK)
