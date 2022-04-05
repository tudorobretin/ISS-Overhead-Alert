import requests
import datetime as dt
import smtplib
import time
import os
from Sunrise_sunset import Hours

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

hours = Hours()

sunrise_sunset = hours.get_sunrise_sunset(city_lat=buc_lat, city_long=buc_long)
sunrise_hour = sunrise_sunset[0]
sunset_hour = sunrise_sunset[1]
current_hour = hours.get_current_hour()

#---logic----------------------


def near():
    if buc_long - 7 < iss_long < buc_long + 7:
        if buc_lat - 7 < iss_lat < buc_lat + 7:
            print("yes")
            return True
    else:
        return False


def is_night():

    if current_hour > sunset_hour or current_hour < sunrise_hour:
        return True

    else:
        return False


def send_mail():
    KEY = os.environ['password']
    my_email = "tudorobretin@gmail.com"
    password = KEY

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        message = f"The ISS is passing over Bucharest and is currently visible; look up!\n\n" \
                  f"ISS latitude: {iss_lat}\n" \
                  f"ISS longitude: {iss_long}\n"
        connection.sendmail(
            from_addr=my_email,
            to_addrs="tudorobre@gmail.com",
            msg=f"Subject:ISS position\n\n{message}"
        )


sent = False
while not sent:

    if is_night():

        if near():
            #print("entered send mail")
            send_mail()
            sent = True


