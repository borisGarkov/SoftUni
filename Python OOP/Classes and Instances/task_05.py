from datetime import datetime, timedelta


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        current_time = datetime(2021, 2, 27, self.hours, self.minutes, self.seconds)
        return f"{current_time.time()}"

    def next_second(self):
        current_time = datetime(2021, 2, 27, self.hours, self.minutes, self.seconds) + timedelta(seconds=1)
        return f"{current_time.time()}"


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())

