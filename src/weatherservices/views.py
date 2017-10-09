from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from weatherservices.utils import validate_input_get_data


@api_view(['GET', 'POST'])
def average_temperature(request):
    if request.method == 'POST':

        return Response(validate_input_get_data(request.data), content_type='application/json', status=status.HTTP_200_OK)
