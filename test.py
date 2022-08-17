import pyowm
import datetime

owm = pyowm.OWM("493c2bef82cd41e33474cbef5053ce59")

joy = input("Enter the city: ")

observation = owm.weather_at_place(joy)
w = observation.get_weather()

sunrise_unix = w.get_sunrise_time()  # default unit: 'unix'
sunrise_iso = w.get_sunrise_time(timeformat='iso')
sunrise_date = w.get_sunrise_time(timeformat='date')
print(sunrise_unix)
print(sunrise_iso)
print(sunrise_date)