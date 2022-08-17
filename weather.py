from PIL import Image, ImageFont, ImageDraw

'''place = "Tashkent"
date = "24 january"
hour = "15:06"
week = "sun"
temp = "+15°"
det_status = "Mainly cloudy"
namlik = "60%"
shamol = "55 m/s"
sunrise = "7:40"
sunset = "18:00"'''

def clear(place, date, hour, week, temp, det_status, namlik, shamol, sunrise, sunset):
	my_image = Image.open("clear.jpg")
	image_editable = ImageDraw.Draw(my_image)

	#SOAT
	soat_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 45)
	soat_text = hour
	w, h = image_editable.textsize(soat_text, font=soat_font)
	image_editable.text((30, 30), soat_text, (255, 255, 255), font=soat_font)

	#SANA 
	sana_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	sana_text = date
	image_editable.text((30, 85), sana_text, (255, 255, 255), font=sana_font)

	#HAFTA_KUNI
	hafta_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	hafta_text = week
	image_editable.text((30, 130), hafta_text, (255, 255, 255), font=hafta_font)

	#PLACE
	place_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 70)
	place_text = place
	w, h = image_editable.textsize(place_text, font=place_font)
	image_editable.text(((1080-w)/2, 80), place_text, (255, 255, 255), font=place_font)

	#NOW
	now_text = "now"
	now_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(now_text, font=now_font)
	image_editable.text(((1080-w2)/2, 160), "now", (255, 255, 255), font=now_font)

	#TEMPERATURA
	temp_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 130)
	temp_text = temp
	#w, h = image_editable.textsize(temp_text, font=temp_font)
	image_editable.text((260, 350), temp_text, (255, 255, 255), font=temp_font)

	#STATUS
	status_text = det_status
	status_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(status_text, font=status_font)
	image_editable.text(((1080-w2)/2, 540), status_text, (255, 255, 255), font=status_font)

	#NAMLIK
	namlik_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	namlik_text = namlik
	image_editable.text((150, 790), namlik_text, (255, 255, 255), font=namlik_font)

	#SHAMOL
	shamol_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	shamol_text = shamol
	image_editable.text((150, 880), shamol_text, (255, 255, 255), font=shamol_font)

	#SUN_RISE
	sunrise_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunrise_text = sunrise
	image_editable.text((610, 960), sunrise_text, (255, 255, 255), font=sunrise_font)

	#SUN_SET
	sunset_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunset_text = sunset
	image_editable.text((830, 960), sunset_text, (255, 255, 255), font=sunset_font)


	#SAVE
	my_image.save("result.jpg")

def rain(place, date, hour, week, temp, det_status, namlik, shamol, sunrise, sunset):
	my_image = Image.open("rainy.jpg")
	image_editable = ImageDraw.Draw(my_image)

	#SOAT
	soat_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 45)
	soat_text = hour
	w, h = image_editable.textsize(soat_text, font=soat_font)
	image_editable.text((30, 30), soat_text, (255, 255, 255), font=soat_font)

	#SANA 
	sana_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	sana_text = date
	image_editable.text((30, 85), sana_text, (255, 255, 255), font=sana_font)

	#HAFTA_KUNI
	hafta_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	hafta_text = week
	image_editable.text((30, 130), hafta_text, (255, 255, 255), font=hafta_font)

	#PLACE
	place_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 70)
	place_text = place
	w, h = image_editable.textsize(place_text, font=place_font)
	image_editable.text(((1080-w)/2, 80), place_text, (255, 255, 255), font=place_font)

	#NOW
	now_text = "now"
	now_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(now_text, font=now_font)
	image_editable.text(((1080-w2)/2, 160), "now", (255, 255, 255), font=now_font)

	#TEMPERATURA
	temp_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 130)
	temp_text = temp
	w, h = image_editable.textsize(temp_text, font=temp_font)
	image_editable.text((270, 385), temp_text, (255, 255, 255), font=temp_font)

	#STATUS
	status_text = det_status
	status_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(status_text, font=status_font)
	image_editable.text(((1080-w2)/2, 620), status_text, (255, 255, 255), font=status_font)

	#NAMLIK
	namlik_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	namlik_text = namlik
	image_editable.text((150, 790), namlik_text, (255, 255, 255), font=namlik_font)

	#SHAMOL
	shamol_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	shamol_text = shamol
	image_editable.text((150, 880), shamol_text, (255, 255, 255), font=shamol_font)

	#SUN_RISE
	sunrise_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunrise_text = sunrise
	image_editable.text((610, 960), sunrise_text, (255, 255, 255), font=sunrise_font)

	#SUN_SET
	sunset_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunset_text = sunset
	image_editable.text((830, 960), sunset_text, (255, 255, 255), font=sunset_font)


	#SAVE
	my_image.save("result.jpg")

def cloud(place, date, hour, week, temp, det_status, namlik, shamol, sunrise, sunset):
	my_image = Image.open("cloudy.jpg")
	image_editable = ImageDraw.Draw(my_image)

	#SOAT
	soat_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 45)
	soat_text = hour
	w, h = image_editable.textsize(soat_text, font=soat_font)
	image_editable.text((30, 30), soat_text, (255, 255, 255), font=soat_font)

	#SANA 
	sana_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	sana_text = date
	image_editable.text((30, 85), sana_text, (255, 255, 255), font=sana_font)

	#HAFTA_KUNI
	hafta_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	hafta_text = week
	image_editable.text((30, 130), hafta_text, (255, 255, 255), font=hafta_font)

	#PLACE
	place_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 70)
	place_text = place
	w, h = image_editable.textsize(place_text, font=place_font)
	image_editable.text(((1080-w)/2, 80), place_text, (255, 255, 255), font=place_font)

	#NOW
	now_text = "now"
	now_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(now_text, font=now_font)
	image_editable.text(((1080-w2)/2, 160), "now", (255, 255, 255), font=now_font)

	#TEMPERATURA
	temp_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 130)
	temp_text = temp
	w, h = image_editable.textsize(temp_text, font=temp_font)
	image_editable.text((290, 402), temp_text, (255, 255, 255), font=temp_font)

	#STATUS
	status_text = det_status
	status_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(status_text, font=status_font)
	image_editable.text(((1080-w2)/2, 600), status_text, (255, 255, 255), font=status_font)

	#NAMLIK
	namlik_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	namlik_text = namlik
	image_editable.text((150, 790), namlik_text, (255, 255, 255), font=namlik_font)

	#SHAMOL
	shamol_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	shamol_text = shamol
	image_editable.text((150, 880), shamol_text, (255, 255, 255), font=shamol_font)

	#SUN_RISE
	sunrise_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunrise_text = sunrise
	image_editable.text((610, 960), sunrise_text, (255, 255, 255), font=sunrise_font)

	#SUN_SET
	sunset_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunset_text = sunset
	image_editable.text((830, 960), sunset_text, (255, 255, 255), font=sunset_font)


	#SAVE
	my_image.save("result.jpg")

def snow(place, date, hour, week, temp, det_status, namlik, shamol, sunrise, sunset):
	my_image = Image.open("snow.jpg")
	image_editable = ImageDraw.Draw(my_image)

	#SOAT
	soat_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 45)
	soat_text = hour
	w, h = image_editable.textsize(soat_text, font=soat_font)
	image_editable.text((30, 30), soat_text, (255, 255, 255), font=soat_font)

	#SANA 
	sana_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	sana_text = date
	image_editable.text((30, 85), sana_text, (255, 255, 255), font=sana_font)

	#HAFTA_KUNI
	hafta_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	hafta_text = week
	image_editable.text((30, 130), hafta_text, (255, 255, 255), font=hafta_font)

	#PLACE
	place_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 70)
	place_text = place
	w, h = image_editable.textsize(place_text, font=place_font)
	image_editable.text(((1080-w)/2, 80), place_text, (255, 255, 255), font=place_font)

	#NOW
	now_text = "now"
	now_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(now_text, font=now_font)
	image_editable.text(((1080-w2)/2, 160), "now", (255, 255, 255), font=now_font)

	#TEMPERATURA
	temp_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 130)
	temp_text = temp
	w, h = image_editable.textsize(temp_text, font=temp_font)
	image_editable.text((290, 380), temp_text, (255, 255, 255), font=temp_font)

	#STATUS
	status_text = det_status
	status_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 60)
	w2, h2 = image_editable.textsize(status_text, font=status_font)
	image_editable.text(((1080-w2)/2, 600), status_text, (255, 255, 255), font=status_font)

	#NAMLIK
	namlik_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	namlik_text = namlik
	image_editable.text((150, 800), namlik_text, (255, 255, 255), font=namlik_font)

	#SHAMOL
	shamol_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	shamol_text = shamol
	image_editable.text((150, 890), shamol_text, (255, 255, 255), font=shamol_font)

	#SUN_RISE
	sunrise_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunrise_text = sunrise
	image_editable.text((650, 960), sunrise_text, (255, 255, 255), font=sunrise_font)

	#SUN_SET
	sunset_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunset_text = sunset
	image_editable.text((860, 960), sunset_text, (255, 255, 255), font=sunset_font)


	#SAVE
	my_image.save("result.jpg")

def sunny(place, date, hour, week, temp, det_status, namlik, shamol, sunrise, sunset):
	my_image = Image.open("sunny.jpg")
	image_editable = ImageDraw.Draw(my_image)

	#SOAT
	soat_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 45)
	soat_text = hour
	w, h = image_editable.textsize(soat_text, font=soat_font)
	image_editable.text((30, 30), soat_text, (255, 255, 255), font=soat_font)

	#SANA 
	sana_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	sana_text = date
	image_editable.text((30, 85), sana_text, (255, 255, 255), font=sana_font)

	#HAFTA_KUNI
	hafta_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	hafta_text = week
	image_editable.text((30, 130), hafta_text, (255, 255, 255), font=hafta_font)

	#PLACE
	place_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 70)
	place_text = place
	w, h = image_editable.textsize(place_text, font=place_font)
	image_editable.text(((1080-w)/2, 80), place_text, (255, 255, 255), font=place_font)

	#NOW
	now_text = "now"
	now_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(now_text, font=now_font)
	image_editable.text(((1080-w2)/2, 160), "now", (255, 255, 255), font=now_font)

	#TEMPERATURA
	temp_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 130)
	temp_text = temp
	w, h = image_editable.textsize(temp_text, font=temp_font)
	image_editable.text((350, 402), temp_text, (255, 255, 255), font=temp_font)

	#STATUS
	status_text = det_status
	status_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(status_text, font=status_font)
	image_editable.text(((1080-w2)/2, 600), status_text, (255, 255, 255), font=status_font)

	#NAMLIK
	namlik_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	namlik_text = namlik
	image_editable.text((150, 800), namlik_text, (255, 255, 255), font=namlik_font)

	#SHAMOL
	shamol_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	shamol_text = shamol
	image_editable.text((150, 890), shamol_text, (255, 255, 255), font=shamol_font)

	#SUN_RISE
	sunrise_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunrise_text = sunrise
	image_editable.text((650, 960), sunrise_text, (255, 255, 255), font=sunrise_font)

	#SUN_SET
	sunset_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunset_text = sunset
	image_editable.text((860, 960), sunset_text, (255, 255, 255), font=sunset_font)



	#SAVE
	my_image.save("result.jpg")

def windy(place, date, hour, week, temp, det_status, namlik, shamol, sunrise, sunset):
	my_image = Image.open("windy.jpg")
	image_editable = ImageDraw.Draw(my_image)

	#SOAT
	soat_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 45)
	soat_text = hour
	w, h = image_editable.textsize(soat_text, font=soat_font)
	image_editable.text((30, 30), soat_text, (255, 255, 255), font=soat_font)

	#SANA 
	sana_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	sana_text = date
	image_editable.text((30, 85), sana_text, (255, 255, 255), font=sana_font)

	#HAFTA_KUNI
	hafta_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	hafta_text = week
	image_editable.text((30, 130), hafta_text, (255, 255, 255), font=hafta_font)

	#PLACE
	place_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 70)
	place_text = place
	w, h = image_editable.textsize(place_text, font=place_font)
	image_editable.text(((1080-w)/2, 80), place_text, (255, 255, 255), font=place_font)

	#NOW
	now_text = "now"
	now_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(now_text, font=now_font)
	image_editable.text(((1080-w2)/2, 160), "now", (255, 255, 255), font=now_font)

	#TEMPERATURA
	temp_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 130)
	temp_text = temp
	w, h = image_editable.textsize(temp_text, font=temp_font)
	image_editable.text((350, 402), temp_text, (255, 255, 255), font=temp_font)

	#STATUS
	status_text = det_status
	status_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(status_text, font=status_font)
	image_editable.text(((1080-w2)/2, 600), status_text, (255, 255, 255), font=status_font)

	#NAMLIK
	namlik_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	namlik_text = namlik
	image_editable.text((150, 800), namlik_text, (255, 255, 255), font=namlik_font)

	#SHAMOL
	shamol_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	shamol_text = shamol
	image_editable.text((150, 890), shamol_text, (255, 255, 255), font=shamol_font)

	#SUN_RISE
	sunrise_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunrise_text = sunrise
	image_editable.text((650, 960), sunrise_text, (255, 255, 255), font=sunrise_font)

	#SUN_SET
	sunset_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunset_text = sunset
	image_editable.text((860, 960), sunset_text, (255, 255, 255), font=sunset_font)



	#SAVE
	my_image.save("result.jpg")

def thunder(place, date, hour, week, temp, det_status, namlik, shamol, sunrise, sunset):
	my_image = Image.open("thunder.jpg")
	image_editable = ImageDraw.Draw(my_image)

	#SOAT
	soat_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 45)
	soat_text = hour
	w, h = image_editable.textsize(soat_text, font=soat_font)
	image_editable.text((30, 30), soat_text, (255, 255, 255), font=soat_font)

	#SANA 
	sana_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	sana_text = date
	image_editable.text((30, 85), sana_text, (255, 255, 255), font=sana_font)

	#HAFTA_KUNI
	hafta_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	hafta_text = week
	image_editable.text((30, 130), hafta_text, (255, 255, 255), font=hafta_font)

	#PLACE
	place_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 70)
	place_text = place
	w, h = image_editable.textsize(place_text, font=place_font)
	image_editable.text(((1080-w)/2, 80), place_text, (255, 255, 255), font=place_font)

	#NOW
	now_text = "now"
	now_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(now_text, font=now_font)
	image_editable.text(((1080-w2)/2, 160), "now", (255, 255, 255), font=now_font)

	#TEMPERATURA
	temp_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 130)
	temp_text = temp
	w, h = image_editable.textsize(temp_text, font=temp_font)
	image_editable.text((330, 390), temp_text, (255, 255, 255), font=temp_font)

	#STATUS
	status_text = det_status
	status_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(status_text, font=status_font)
	image_editable.text(((1080-w2)/2, 580), status_text, (255, 255, 255), font=status_font)

	#NAMLIK
	namlik_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	namlik_text = namlik
	image_editable.text((170, 780), namlik_text, (255, 255, 255), font=namlik_font)

	#SHAMOL
	shamol_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	shamol_text = shamol
	image_editable.text((170, 870), shamol_text, (255, 255, 255), font=shamol_font)

	#SUN_RISE
	sunrise_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunrise_text = sunrise
	image_editable.text((630, 940), sunrise_text, (255, 255, 255), font=sunrise_font)

	#SUN_SET
	sunset_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunset_text = sunset
	image_editable.text((840, 940), sunset_text, (255, 255, 255), font=sunset_font)



	#SAVE
	my_image.save("result.jpg")

def fog(place, date, hour, week, temp, det_status, namlik, shamol, sunrise, sunset):
	my_image = Image.open("fog.jpg")
	image_editable = ImageDraw.Draw(my_image)

	#SOAT
	soat_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 45)
	soat_text = hour
	w, h = image_editable.textsize(soat_text, font=soat_font)
	image_editable.text((30, 30), soat_text, (255, 255, 255), font=soat_font)

	#SANA 
	sana_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	sana_text = date
	image_editable.text((30, 85), sana_text, (255, 255, 255), font=sana_font)

	#HAFTA_KUNI
	hafta_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	hafta_text = week
	image_editable.text((30, 130), hafta_text, (255, 255, 255), font=hafta_font)

	#PLACE
	place_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 70)
	place_text = place
	w, h = image_editable.textsize(place_text, font=place_font)
	image_editable.text(((1080-w)/2, 80), place_text, (255, 255, 255), font=place_font)

	#NOW
	now_text = "now"
	now_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(now_text, font=now_font)
	image_editable.text(((1080-w2)/2, 160), "now", (255, 255, 255), font=now_font)

	#TEMPERATURA
	temp_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 130)
	temp_text = temp
	w, h = image_editable.textsize(temp_text, font=temp_font)
	image_editable.text((330, 390), temp_text, (255, 255, 255), font=temp_font)

	#STATUS
	status_text = det_status
	status_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(status_text, font=status_font)
	image_editable.text(((1080-w2)/2, 580), status_text, (255, 255, 255), font=status_font)

	#NAMLIK
	namlik_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	namlik_text = namlik
	image_editable.text((170, 780), namlik_text, (255, 255, 255), font=namlik_font)

	#SHAMOL
	shamol_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	shamol_text = shamol
	image_editable.text((170, 870), shamol_text, (255, 255, 255), font=shamol_font)

	#SUN_RISE
	sunrise_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunrise_text = sunrise
	image_editable.text((630, 940), sunrise_text, (255, 255, 255), font=sunrise_font)

	#SUN_SET
	sunset_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunset_text = sunset
	image_editable.text((840, 940), sunset_text, (255, 255, 255), font=sunset_font)



	#SAVE
	my_image.save("result.jpg")

def cold(place, date, hour, week, temp, det_status, namlik, shamol, sunrise, sunset):
	my_image = Image.open("cold.jpg")
	image_editable = ImageDraw.Draw(my_image)

	#SOAT
	soat_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 45)
	soat_text = hour
	w, h = image_editable.textsize(soat_text, font=soat_font)
	image_editable.text((30, 30), soat_text, (255, 255, 255), font=soat_font)

	#SANA 
	sana_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	sana_text = date
	image_editable.text((30, 85), sana_text, (255, 255, 255), font=sana_font)

	#HAFTA_KUNI
	hafta_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 40)
	hafta_text = week
	image_editable.text((30, 130), hafta_text, (255, 255, 255), font=hafta_font)

	#PLACE
	place_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 70)
	place_text = place
	w, h = image_editable.textsize(place_text, font=place_font)
	image_editable.text(((1080-w)/2, 80), place_text, (255, 255, 255), font=place_font)

	#NOW
	now_text = "now"
	now_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(now_text, font=now_font)
	image_editable.text(((1080-w2)/2, 160), "now", (255, 255, 255), font=now_font)

	#TEMPERATURA
	temp_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 130)
	temp_text = temp
	w, h = image_editable.textsize(temp_text, font=temp_font)
	image_editable.text((330, 390), temp_text, (255, 255, 255), font=temp_font)

	#STATUS
	status_text = det_status
	status_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	w2, h2 = image_editable.textsize(status_text, font=status_font)
	image_editable.text(((1080-w2)/2, 580), status_text, (255, 255, 255), font=status_font)

	#NAMLIK
	namlik_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	namlik_text = namlik
	image_editable.text((170, 780), namlik_text, (255, 255, 255), font=namlik_font)

	#SHAMOL
	shamol_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	shamol_text = shamol
	image_editable.text((170, 870), shamol_text, (255, 255, 255), font=shamol_font)

	#SUN_RISE
	sunrise_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunrise_text = sunrise
	image_editable.text((630, 940), sunrise_text, (255, 255, 255), font=sunrise_font)

	#SUN_SET
	sunset_font = ImageFont.truetype('RobotoSlab-SemiBold.ttf', 50)
	sunset_text = sunset
	image_editable.text((840, 940), sunset_text, (255, 255, 255), font=sunset_font)



	#SAVE
	my_image.save("result.jpg")
