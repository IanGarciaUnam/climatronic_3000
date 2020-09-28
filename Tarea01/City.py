import requests
# Clase que modela una ciudad en función de temperatura
class City:
    def __init__(self, nombre, temperatura, descripcion):
        self.nombre = nombre
        self.temperatura = temperatura
        self.descripcion = descripcion

    def printCity(self):
        d = {"Ciudad" : self.nombre, "Temperatura" : self.temperatura, "Descripción" : self.descripcion,}
        return d
        
f = open("/home/david/Documentos/Modelado_Y_Programacion/WeatherApp/src/python/cities.txt", "r")
conjunto = set()
for x in f:
  conjunto.add(x.rstrip("\n"))
f.close()

api_adrees = 'http://api.openweathermap.org/data/2.5/weather?appid=1bfd917ba8b375efeea803bf7b9b1ee0&q='

for city in conjunto:
  url = api_adrees + city

  json_data = requests.get(url).json()

  cities = City(city,  json_data['main']['temp'], json_data['weather'][0]['description'])

  print(cities.printCity()) 