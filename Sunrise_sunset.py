import requests
import datetime as dt

class Hours:
    def __init__(self):
        self.a = 0

    def get_sunrise_sunset(self, city_lat, city_long):
        sun_parameters = {
            "lat": city_lat,
            "lng": city_long,
            "formatted": 0
        }
        sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=sun_parameters)
        sun_response.raise_for_status()
        data = sun_response.json()

        sunrise = data['results']['sunrise']
        sunrise_hour = int(sunrise.split('T')[1].split(":")[0]) + 3

        sunset = data['results']['sunset']
        sunset_hour = int(sunset.split('T')[1].split(":")[0]) + 3

        return (sunrise_hour, sunset_hour)

    def get_current_hour(self):
        time_now = dt.datetime.now()
        time_now_hour = time_now.hour
        return time_now_hour
