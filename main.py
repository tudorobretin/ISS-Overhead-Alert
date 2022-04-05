import requests
import datetime as dt
import smtplib
import time
import os
from send_mail import Send

# ---Iss & Bucharest position-----------------

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = iss_response.json()
iss_lat = float(data["iss_position"]['latitude'])
iss_long = float(data["iss_position"]["longitude"])
position = (iss_lat, iss_long)
# print(position)

buc_lat = 44.426765
buc_long = 26.102537
# buc_lat = -38
# buc_long = 153


# ---Sunrise and sunset----------------

sun_parameters_bucharest = {
    "lat": buc_lat,
    "lng": buc_long,
    "formatted": 0
}
sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=sun_parameters_bucharest)
sun_response.raise_for_status()
data = sun_response.json()
#print(data)
sunrise = data['results']['sunrise']
sunrise_hour = int(sunrise.split('T')[1].split(":")[0]) + 3
#print(sunrise_hour)
sunset = data['results']['sunset']
sunset_hour = int(sunset.split('T')[1].split(":")[0]) + 3
#print(sunset_hour)

# ---time now---------------------

time_now = dt.datetime.now()
time_now_hour = time_now.hour + 3
#print(time_now_hour)


#---logic----------------------


def near():
    if buc_long - 7 < iss_long < buc_long + 7:
        if buc_lat - 7 < iss_lat < buc_lat + 7:
            print("yes")
            return True
    else:
        return False


def is_night():

    if time_now_hour > sunset_hour or time_now_hour < sunrise_hour:
        return True

    else:
        return False


send = Send()


sent = False
while not sent:

    if is_night():

        if near():
            #print("entered send mail")
            send.mail()
            sent = True


