from datetime import datetime
now = datetime.now()


def get_local_date():
	months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
	day=now.day
	month = months[now.month - 1]
	year = now.year
	messsage = "{} de {} del {}".format(day, month, year)
	return messsage
def get_hour():
	return now.hour
def get_local_time():
	hora=int(now.hour)
	minute=now.minute
	sun='a m'
	if hora > 12:
		hora=hora-12
		sun='pm'
	messsage="{} Horas con {} minutos {}".format(hora, minute,sun)
	return messsage

def get_year():
	return now.year
def get_month():
	return now.month
def get_day():
	return now.day
def get_sun():
	if int(now.hour) > 12:
		return 'PM'
	return 'AM'
