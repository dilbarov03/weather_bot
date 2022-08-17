from weather import *
from weekday import *
import pyowm
import datetime

owm = pyowm.OWM("493c2bef82cd41e33474cbef5053ce59")

joy = input("Enter the city: ")

observation = owm.weather_at_place(joy)
w = observation.get_weather()
t = w.get_temperature('celsius')
temp2 = t["temp"]
temp2 = round(temp2, 1)
temp2 = str(temp2)+"°"
sh=w.get_wind()
namlik=w.get_humidity()
sh1=sh["speed"]
sunrise_date = w.get_sunrise_time(timeformat='date')
sunsen_date = w.get_sunset_time(timeformat='date')

sana = day()
soat = hour()
hafta = weekday()
#holat = w.get_status().lower()
holat = w.get_detailed_status()

qch1=str(sunrise_date)[11:16]
ert1=int(qch1[0:2])+5
ert2=(qch1[3::])
sunr=f"{ert1}:{ert2}"

qch2=str(sunsen_date)[11:16]
ert3=int(qch2[0:2])+5
ert4=(qch2[3::])
suns=f"{ert3}:{ert4}"

if w.get_status().lower()=="rain" or w.get_status().lower()=="rainy":
	rain(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
elif w.get_status().lower()=="sun":
	sunny(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
elif w.get_status().lower()=="clouds":
	cloud(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
elif w.get_status().lower()=="fog":
	fog(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
elif w.get_status().lower()=="haze":
	fog(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
elif w.get_status().lower()=="mist":
	fog(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
elif w.get_status().lower()=="snow":
	snow(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
elif w.get_status().lower()=="storm":
	windy(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
elif w.get_status().lower()=="hurricane":
	windy(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
elif w.get_status().lower()=="wind":
	windy(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
elif w.get_status().lower()=="windy":
	windy(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
elif w.get_status().lower()=="light":
	clear(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
elif w.get_status().lower()=="clear":
	clear(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
	#print(joy, sana, soat, hafta, temp2, holat, namlik, sh1, qch1, qch2)
elif w.get_status().lower()=="hot":
	sunny(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
elif w.get_status().lower()=="cold":
	cold(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
