
import os
import random
from gtts import gTTS
from playsound import playsound
import Tiempo as time

from Tiempo import Tiempo

class Voz:
	""" Conversion de Texto a Voz motor del habla del climatrón para el anuncio del clima. 
	 Atributos
	 ----------
	 tiempo = Tiempo()
	 	El tiempo de un día
	"""
	def __init__(self):
		""" Constructor que tiene como atributo el tiempo """
		self.tiempo = Tiempo()

	def say(self, word):
		""" Recibe una frase y hace que gtts guarde en un archivo de voz el contenido de la frase y lo reproduzca. 
		 Parametros
		 -----------
		 word : str
		 	palabra a decir por gtts

		"""
		my_word = str(word)
		tts = gTTS(my_word, lang = 'es-us') # Frase e idioma en el que la voz será
		tts.save("resources/speaking.mp3")	
		playsound("resources/speaking.mp3")

	def say_slow(self, word):
		""" Recibe una frase y hace que gtts guarde en un archivo de voz el contenido de la frase y lo reproduzca lentamente.
		 Parametros
		 -----------
		 word : str
		  palabra a decir por gtts
		"""
		my_word = str(word)
		tts = gTTS(my_word, lang = 'es-us', slow = True)
		tts.save("resources/speaking.mp3")	
		playsound("resources/speaking.mp3")

	def save_audio(self, word):
		""" Recibe una frase y hace que gtts guarde en un archivo de voz el contenido de la frase.
		 Parametros
		 -----------
		 word : str
		  palabra a decir por gtts y guardar en un audio
		"""
		my_word = str(word)
		tts=gTTS(my_word, lang = 'es-us')
		tts.save("resources/saved.mp3")

	def say_saved_audio(self):
		""" Reproduce el audio del archiv0 saved.mp3 """
		playsound("resources/saved.mp3")

	def into_start(self):
		""" Reproduce el audio del archivp announcement.mp3 """
		playsound("resources/tones/announcement.mp3")


	def greet(self):
		""" Lee un archivo dependiendo si la hora es AM o PM y hace que el asistente de voz lo lea"""
		if self.tiempo.get_sun() == 'AM':
			saludo = open("resources/greeting/greeting_morning.txt","r")
			text = saludo.read().split(',')
			saludo.close()
			chosen = str(random.choice(text)) # Selecciona saludo random
			self.say(chosen) # El asistente de voz lee
		if self.tiempo.get_sun() == 'PM':
			saludo = open("resources/greeting/greeting_afternoon.txt","r")
			text = saludo.read().split(',')
			saludo.close()
			chosen = str(random.choice(text))  #Selecciona saludo random
			self.say(chosen) # El asistente de voz lee


