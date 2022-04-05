# Snake Game
A python script that emails you and your friends when the international space station is visible from Bucharest.

## Features and used concepts:

    -Necesary information is taken from ISS API and Sunrise-sunset.org API
    -Uses environment variables to store and use email password

Features:
- Gets sunrise and sunset times from API call
- Gets ISS lat/long coordinates from API call
- Compares current hour to sunset/sunrise to determine if it's dark outside
- Compares ISS coordinates to Bucharest coordinates 
- Sends email using smtp library

*Ideally this script would be hosted and ran every 30 minutes for full functionality


![](https://github.com/tudorobretin/Snake-Game/blob/readme/Snake.gif)


        