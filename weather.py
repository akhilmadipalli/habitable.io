import requests
from dotenv import load_dotenv
import os
from geopy import Nominatim
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv("API_KEY")


@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: float


def get_lat_lon(city_name):
    geolocator = Nominatim(user_agent="habitable.me")
    city = geolocator.geocode(city_name)
    lat = city.latitude
    lon = city.longitude
    return lat, lon


def get_current_weather(lat, lon, API_key):
    resp = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=imperial"
    ).json()
    data = WeatherData(
        main=resp.get("weather")[0].get("main"),
        description=resp.get("weather")[0].get("description"),
        icon=resp.get("weather")[0].get("icon"),
        temperature=resp.get("main").get("temp"),
    )
    return data


def main(city_name):
    lat, lon = get_lat_lon(city_name)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data


if __name__ == "__main__":
    lat, lon = get_lat_lon("Blacksburg")
    print(get_current_weather(lat, lon, api_key))
