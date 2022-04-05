import requests


class GetPosition:
    def __init__(self):
        self.a = 0

    def iss(self):
        iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
        data = iss_response.json()
        iss_lat = float(data["iss_position"]['latitude'])
        iss_long = float(data["iss_position"]["longitude"])
        position = (iss_lat, iss_long)
        return position

    def bucharest(self):
        buc_lat = 44.426765
        buc_long = 26.102537
        position = (buc_lat, buc_long)
        return position
