import sqlite3
import random
import logging
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from weather import *
from weekday import *
import pyowm
import datetime

owm = pyowm.OWM("TOKEN")
mgr = owm.weather_manager()


bot = Bot(token="TOKEN")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def send_welcome(message):
	await bot.send_message(message.chat.id, "Hi. Welcome to Weather Bot. \nI can find current weather in your city.\nJust send me a message.")

@dp.message_handler()
async def send_all(message: types.Message):
	try:
		joy = message.text

		observation = mgr.weather_at_place(joy)
		w = observation.weather
		t = w.temperature('celsius')
		temp2 = t["temp"]
		temp2 = round(temp2, 1)
		temp2 = str(temp2)+"°"
		sh=w.wind()
		namlik=w.humidity
		sh1=sh["speed"]
		sunrise_date = w.sunrise_time(timeformat='date')
		sunsen_date = w.sunset_time(timeformat='date')

		sana = day()
		soat = hour()
		hafta = weekday()
		#holat = w.status.lower()
		holat = w.detailed_status

		qch1=str(sunrise_date)[11:16]
		ert1=int(qch1[0:2])+5
		ert2=(qch1[3::])
		sunr=f"{ert1}:{ert2}"

		qch2=str(sunsen_date)[11:16]
		ert3=int(qch2[0:2])+5
		ert4=(qch2[3::])
		suns=f"{ert3}:{ert4}"

		if w.status.lower()=="rain" or w.status.lower()=="rainy":
			rain(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
		elif w.status.lower()=="sun":
			sunny(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
		elif w.status.lower()=="clouds":
			cloud(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
		elif w.status.lower()=="fog":
			fog(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
		elif w.status.lower()=="haze":
			fog(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
		elif w.status.lower()=="mist":
			fog(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
		elif w.status.lower()=="snow":
			snow(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
		elif w.status.lower()=="storm":
			windy(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
		elif w.status.lower()=="hurricane":
			windy(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
		elif w.status.lower()=="wind":
			windy(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
		elif w.status.lower()=="windy":
			windy(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
		elif w.status.lower()=="light":
			clear(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
		elif w.status.lower()=="clear":
			clear(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
			#print(joy, sana, soat, hafta, temp2, holat, namlik, sh1, qch1, qch2)
		elif w.status.lower()=="hot":
			sunny(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
		elif w.status.lower()=="cold":
			cold(joy, str(sana), soat, hafta, str(temp2), holat, f"{str(namlik)}%", f"{str(sh1)} m/s", str(qch1), str(qch2))
		
		photo = open('result.jpg', 'rb')
		await bot.send_photo(message.chat.id, photo, caption="Done✅")
		await bot.send_message(message.chat.id, f"Send the name of the place to get current weather")

	except:
		await bot.send_message(message.chat.id, f"Sorry, I could not find anything.")

if __name__ == '__main__':
	executor.start_polling(dp)
