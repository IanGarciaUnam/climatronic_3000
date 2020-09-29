"""
 	Voz 
	Conversion de Texto a Voz motor del habla del climatrón para el anuncio del clima 


"""
import os
import random
from gtts import gTTS
from playsound import playsound
#import speech_recognition as sr
import tiempo as time




def say(word):
		my_word=str(word)
		tts=gTTS(my_word, lang = 'es-us')
		tts.save("resources/speaking.mp3")	
		playsound("resources/speaking.mp3")

def say_slow(word):
		my_word=str(word)
		tts=gTTS(my_word, lang = 'es-us', slow = True)
		tts.save("resources/speaking.mp3")	
		playsound("resources/speaking.mp3")

def save_audio(word):
		my_word=str(word)
		tts=gTTS(my_word, lang = 'es-us')
		tts.save("resources/saved.mp3")

def say_saved_audio():
		playsound("resources/saved.mp3")

def into_start():
	playsound("resources/tones/announcement.mp3")


def greet():
	if time.get_sun() == 'AM':
		saludo = open("resources/greeting/greeting_morning.txt","r")
		text=saludo.read().split(',')
		saludo.close()
		chosen=str(random.choice(text))
		say(chosen)
	if time.get_sun() == 'PM':
		saludo = open("resources/greeting/greeting_afternoon.txt","r")
		text=saludo.read().split(',')
		saludo.close()
		chosen=str(random.choice(text))
		say(chosen)


