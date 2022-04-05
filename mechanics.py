class Compare:
    def __init__(self):
        self.a = 0


    def is_near(buc_lat, buc_long, iss_lat, iss_long):
        if buc_long - 7 < iss_long < buc_long + 7:
            return buc_lat - 7 < iss_lat < buc_lat + 7
        else:
            return False


    def is_night(sunset_hour, sunrise_hour, current_hour):
        if current_hour > sunset_hour or current_hour < sunrise_hour:
            return True

        else:
            return False
