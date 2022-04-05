# ISS-Overhead-Alert
A python script that emails you and your friends when the international space station is visible from Bucharest.

## Features and used concepts:

    -Necesary information is taken from ISS API and Sunrise-sunset.org API
    -Uses environment variables to store and use email password
    -Project structured using OOP

Features:
- Gets sunrise and sunset times from API call
- Gets ISS lat/long coordinates from API call
- Compares current hour to sunset/sunrise to determine if it's dark outside
- Compares ISS coordinates to Bucharest coordinates 
- Sends email using smtp library

*Ideally this script would be hosted and ran every 30 minutes for full functionality
*needs bug fix to deal with city change and error cause by different time zone
*needs other method of getting time now, to adapt for city changes

![](https://github.com/tudorobretin/ISS-Overhead-Alert/blob/master/iss_mail.png)


        