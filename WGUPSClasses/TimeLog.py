

# A class to handle the parsing and formatting of times in the application.
class TimeLog:
    def __init__(self):
        # Default class constructor, has no parameters.
        self.current_hour = 8
        self.current_minute = 0
        self.current_time = self.format_current_time(self.current_hour, self.current_minute)
        self.status_change_log = []

    # Formats the current time. Takes an hour and a minute integer and returns a string.
    def format_current_time(self, hour, minute):
        ampm = ' AM'
        if hour > 12:
            hour = hour - 12
            ampm = ' PM'
        if minute < 10:
            minute = '0' + '{:.2f}'.format(minute)
        else:
            minute = '{:.2f}'.format(minute)
        return str(hour) + ':' + minute + ampm

    # Returns the length of time, in minutes, it will take the truck to travel a given distance.
    def calculate_minutes_from_distance(self, avg_truck_speed, distance):
        return distance / avg_truck_speed * 60

    # Returns the time after incrementing it by the given hour and minute values.
    def increment_current_time(self, truck_hour, truck_minute, hour_increment, minute_increment):
        new_truck_hour = truck_hour + hour_increment
        new_truck_minute = 0
        if truck_minute + minute_increment >= 60:
            new_truck_hour += 1
            new_truck_minute = (truck_minute + minute_increment) - 60
        else:
            new_truck_minute = truck_minute + minute_increment
        return new_truck_hour, new_truck_minute

    # Returns whether time1 is after time2 as a boolean value.
    def is_after(self, time1, time2):
        time1 = time1.split(':')
        time2 = time2.split(':')
        hour1 = int(time1[0])
        hour2 = int(time2[0])
        minute1 = float(time1[1].split(' ')[0])
        minute2 = float(time2[1].split(' ')[0])
        ampm1 = time1[1].split(' ')[1]
        ampm2 = time2[1].split(' ')[1]
        if ampm1 > ampm2:
            return True
        elif ampm2 > ampm1:
            return False
        else:
            if hour1 == hour2:
                return True if minute1 > minute2 else False
            else:
                return True if hour1 > hour2 else False
