import datetime

def weekday():
	x = datetime.datetime.now()
	weekday=x.strftime("%A")
	day=x.strftime("%A")
	month=x.strftime("%m")
	hafta={
	"Monday": "mon",
	"Tuesday": "tue",
	"Wednesday": "wed",
	"Thursday": "thu",
	"Friday": "fri",
	"Saturday": "sat",
	"Sunday": "sun"
	}

	#return hafta[weekday]
	ee=x.strftime("%a")
	return ee

def day():
	x = datetime.datetime.now()
	day1=x.strftime("%d")
	mon_n=x.strftime("%B")

	st = f"{day1}-{mon_n}"
	return st

def hour():
	x = datetime.datetime.now()
	h1=x.strftime("%H:"+"%M")
	yy=x.strftime("%H")
	gg=int(yy)
	dd=str(gg)
	mm=x.strftime("%M")

	l=f"{dd}:{mm}"
	return l

#print(hour())

def month():
	x = datetime.datetime.now()
	mon_n=x.strftime("%m")
	return mon_n
