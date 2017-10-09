# Weather Services

A Django python app that integrates with a mock api that exposes access to three different weather services.

Returns average temperature from services chosen.

You can either enter a lat and a lng or a zip code which will be converted to lat and lng.

Lat and lng takes precedence over zip code, so if both are entered the lat and lng will be used.

There are various validations on the fields and integrates with google maps api to validate both lat and lng and zip code.

Make sure to enter your google maps api key in weatherservices/settings_secrets.py.

### Setup
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python src/manage.py runserver
```

### Docker
```
docker-compose up -d --build
```

### Routes
Host: http://127.0.0.1:8000/

POST /temperature/
```json
{
	"lat": 10,
	"lng": -43.53,
	"zip_code": 78758,
	"filters": [
		"noaa",
		"weather.com",
		"accuweather"
	]
}
```