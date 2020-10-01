from Voz import Voz
from City import City
import requests
import os

voice = Voz()
path = str(os.getcwd()) #Obtiene la ruta relativa en la computadora de trabajo actual
file = open(path+"/cities.txt", "r")#archivo de lectura
conjunto = set()
for x in file:
  conjunto.add(x.rstrip("\n"))
file.close()

api_adrees = 'http://api.openweathermap.org/data/2.5/weather?appid=1bfd917ba8b375efeea803bf7b9b1ee0&q=' # Llave del API para obtener info

for city in conjunto:
  url = api_adrees + city
  
  json_data = requests.get(url).json()

  ciudad = City(city, json_data['main']['temp'], json_data['weather'][0]['description'])
  print(ciudad)
  voice.into_start()
  voice.greet()
  voice.say(ciudad.formato())


