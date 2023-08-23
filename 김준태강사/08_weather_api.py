import json

import requests

cities = {
    'Seoul': {'latitude': 37.566, 'longitude': 126.9784},
    'London': {'latitude': 51.5085, 'longitude': -0.1257},
    'New York': {'latitude': 40.7143, 'longitude': -74.006}
}


def get_temperature(location) -> str:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={location['latitude']}&longitude={location['longitude']}&current_weather=true"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['current_weather']['temperature']


for city, location in cities.items():
    print(f"{city}의 날Tl : {get_temperature(location)}도")
