import requests
import datetime as dt
import smtplib
import time
import os
from send_mail import Send
from mechanics import Compare
from iss_position import GetPosition
from Sunrise_sunset import Hours

# ---Iss & Bucharest position-----------------

get_position = GetPosition()

iss_position = get_position.iss()
iss_lat = iss_position[0]
iss_long = iss_position[1]

buc_position = get_position.bucharest()
buc_lat = buc_position[0]
buc_long = buc_position[1]

# ---Sunrise and sunset----------------

hours = Hours()

sunrise_sunset = hours.get_sunrise_sunset(city_lat=buc_lat, city_long=buc_long)
sunrise_hour = sunrise_sunset[0]
sunset_hour = sunrise_sunset[1]
current_hour = hours.get_current_hour()

#---logic----------------------

send = Send()
compare = Compare()

sent = False
while not sent:

    if compare.is_night():

        if compare.is_night():
            send.mail()
            sent = True


