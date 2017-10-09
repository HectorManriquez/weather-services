from googlemaps import Client

from weatherservices.settings_secrets import GOOOGLE_MAPS_API_KEY

gmaps = Client(key=GOOOGLE_MAPS_API_KEY)
