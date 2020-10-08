from datetime import datetime

class Tiempo:
	"""Clase que modela el tiempo dado el año, mes, día y hora."""
	def __init__(self):
		""" Constructor que tiene como atributo el tiempo real."""
		self.now = datetime.now()
	def get_local_date(self):
		""" Regresa la fecha local."""
		months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
		day = self.now.day
		month = months[self.now.month - 1]
		year = self.now.year
		messsage = "{} de {} del {}".format(day, month, year)
		return messsage
	def get_hour(self):
		""" Regresa la hora local."""
		return self.now.hour
	def get_local_time(self):
		""" Regresa la tienpo local (AM) o (PM)."""
		hora = int(self.now.hour)
		minute = self.now.minute
		sun = 'am'
		if hora > 12:
			hora=hora-12
			sun='pm'
		messsage="{} Horas con {} minutos {}".format(hora, minute,sun)
		return messsage

	def get_year(self):
		""" Regresa el año actual. """
		return self.now.year
	def get_month(self):
		""" Regresa el mes actual. """
		return self.now.month
	def get_day(self):
		""" Regresa el día actual. """
		return self.now.day
	def get_sun(self):
		""" Regresa la hora AM o PM """
		if int(self.now.hour) > 12:
			return 'PM'
		return 'AM'

	def convert_into_hour(self,hora_string):
		"""Regresa una hora convertida en fecha"""
		text = str(hora_string)
		hora = datetime.strptime(text, '%H:%M')
		return hora #str(hora.hour) + " y " + str(hora.minute) + select
