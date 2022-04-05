import os
import smtplib


class Send():
    def __init__(self):
        self.a = 0

    def mail(self, iss_lat, iss_long):
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
