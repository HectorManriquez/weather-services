# Weather Services

A Django python app that integrates with a mock api that exposes access to three different weather services.

Returns average temperature from services chosen.

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
	"filters": [
		"noaa",
		"weather.com",
		"accuweather"
	]
}
```