import requests
import os
from googletrans import Translator
from Tiempo import Tiempo
import datetime
class City:


  def __init__(self, nombre, temperatura, descripcion):
   """ Contructor a partir del nombre, temperatura y descripción"""
   self.nombre = nombre
   self.temperatura = int(temperatura - 273.15) # La temperatura del API está en Kelvin, los convertimos a °C
   self.transalator = Translator() # Tradcutor para la descripción del cielo
   self.descripcion = self.transalator.translate(descripcion, src = 'en', dest = 'es').text
   self.hora_salida=None
   self.hora_llegada=None

  def set_hora_salida(self, hora_salida):
    tiempo=Tiempo()
    self.hora_salida=tiempo.convert_into_hour(str(hora_salida))

  def set_hora_llegada(self, hora_llegada):
    tiempo=Tiempo()
    self.hora_llegada=tiempo.convert_into_hour(str(hora_llegada))


  def imprime_ciudad(self):
    """ Regresa un diccionario con la información de la ciudad"""
    d = "{ Ciudad : self.nombre, \"Temperatura\" :"+ str(self.temperatura) + "\"°C\", \"Descripción\" : "+self.descripcion+",}"
    return d

  def formato(self):
    """ Regresa una cadena con la información en formato para que el asistente de voz lo diga"""

    return "Pasajeros con destino a "+ self.nombre+ ", se encuentra con una temperatura de "+ str(self.temperatura) +" Grados Centigrados, Y con "+ self.descripcion

  def formato_salida(self):
    """Regresa una cadena con la informacion lista para ser dicha por la asistente de voz dando información de la hora"""
    if self.temperatura==None or self.descripcion == None:
      return "Vuelo proximo a salir con horario de las " + str(self.hora_salida) + " y Destino " + str(self.nombre) + "Excelente viaje"
    return "Vuelo con salida de las "+ str(self.hora_salida.hour) + "horas , y"+ str(self.hora_salida.minute) +" minutos, con Destino como " + str(self.nombre) + " Tiene una temperatura de " + str(self.temperatura)+ "Grados Centigrados y con" + str(self.descripcion) 


  def get_nombre(self):
    """ Regresa el nombre de la ciudad """
    return str(self.nombre)

  def get_temperatura(self):
    """ Regresa la temperatura de la ciudad """
    return str(self.temperatura)

  def get_descripcion_clima(self):
    """ Regresa la descripción de la ciudad """
    return str(self.descripcion)

  def __gt__(self, ciudad):
    if self.hora_salida==None or ciudad.hora_salida==None:
      return self.temperatura > ciudad.temperatura
    return self.hora_salida > ciudad.hora_salida
    
  def __str__(self):
    return "Ciudad:" + self.nombre +" Temperatura:" + str(self.temperatura)+" °C"+ " Cielo:"+ self.descripcion
  


