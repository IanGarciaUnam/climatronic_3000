import requests
import os
from googletrans import Translator
from Tiempo import Tiempo
from datetime import datetime
class City:
  """ Clase que representa una ciudad.
   
    Atributos
    ----------
    nombre : str
       nombre de la ciudad
    temperatura : float
        temperatura de la ciudad
    translator : Translator()
        traductor
    descripcion : str
        descripción de la ciudad
    hora_salida : str
      hora de salida de una ciudad
    hora_llegada : str
      hora de llegada de una ciudad
    humedad : int
      humedad de una ciudad
    temp_max : int
      temperatura máxima de una ciudad
    temp_min : int
      temperatura minima de una ciudad
  """

  def __init__(self, nombre, temperatura, descripcion, humedad, temp_max, temp_min):
   """ Contructor a partir del nombre, temperatura y descripción
    Parametros
    ----------
    nombre : str
      El nombre de la ciudad
    temperatura : float
      La temperatura de la ciudad
    descripcion : str
      La descripción de la ciudad
    humedad : int
      La humedad de la ciudad
    temp_max : float
     La temperatura máxima de la ciudad
    temp_min : float
     La temperatura mínima de la ciudad

    Returns
    --------
    Una instacia de ciudad
    """

   self.nombre = nombre
   self.temperatura = int(temperatura - 273.15) # La temperatura del API está en Kelvin, los convertimos a °C
   self.transalator = Translator() # Tradcutor para la descripción del cielo
   self.descripcion = self.transalator.translate(descripcion, src = 'en', dest = 'es').text
   self.hora_salida = None # Hora de salida si la ciudad es del dataset1
   self.hora_llegada = None # Hora de llegada si la ciudad es del dataset1
   self.humedad = humedad
   self.temp_max = int(temp_max - 273.15)
   self.temp_min = int(temp_min -273.15)

  def set_hora_salida(self, hora_salida):
    """ Define la hora de salida del vuelo de la ciudad 
     Parametros
     -----------
     hora_salida : str
      La hora de salida de la ciudad
    """
    tiempo = Tiempo()
    self.hora_salida = tiempo.convert_into_hour(str(hora_salida))

  def set_hora_llegada(self, hora_llegada):
     """ Define la hora de llegada del vuelo de la ciudad 
      Parametros
     -----------
      hora_llegada : str
        La hora de llegada de la ciudad
     """
     tiempo = Tiempo()
     self.hora_llegada = tiempo.convert_into_hour(str(hora_llegada))


  def imprime_ciudad(self):
    """ Regresa un diccionario con la información de la ciudad"""
    d = "{ Ciudad : self.nombre, \"Temperatura\" :"+ str(self.temperatura) + "\"°C\", \"Descripción\" : "+self.descripcion+",}"
    return d

  def formato(self):
    """ Regresa una cadena con la información en formato para que el asistente de voz lo diga"""

    return "PROXIMO A ABORDAR: "+ self.nombre+ ", TEMPERATURA: "+ str(self.temperatura) +" °C, CIELO: "+ self.descripcion + " HÚMEDAD: " + str(self.humedad)+"%" + "  [SALIDA: " +  str(self.hora_salida.hour)+":"+str(self.hora_salida.minute) + " hrs]"

  def formato_salida(self):
    """Regresa una cadena con la informacion lista para ser dicha por la asistente de voz dando información de la hora"""
    if self.temperatura == None or self.descripcion == None:
      return "Vuelo proximo a salir con horario de las " + str(self.hora_salida) + " y Destino " + str(self.nombre) + "Excelente viaje"
    return "Vuelo con salida de las "+ str(self.hora_salida.hour) + "horas , i"+ str(self.hora_salida.minute) +" minutos, con Destino como " + str(self.nombre) + " Tiene una temperatura de " + str(self.temperatura)+ "Grados Centigrados,   cielo con "+str(self.descripcion) + " y con una húmedad de " + str(self.humedad) + " porciento. Feliz Viaje" 


  def get_nombre(self):
    """ Regresa el nombre de la ciudad """
    return str(self.nombre)

  def get_temperatura(self):
    """ Regresa la temperatura de la ciudad """
    return str(self.temperatura)

  def get_descripcion_clima(self):
    """ Regresa la descripción de la ciudad """
    return str(self.descripcion)
  
  def get_humedad(self):
    """ Regresa la humedad de la ciudad """
    return str(self.humedad)

  def get_temp_min(self):
    """ Regresa la temperatura minima """
    return str(self.temp_min)

  def get_temp_max(self):
    """ Regresa la temperatura máxima """
    return str(self.temp_max)

  
  def __gt__(self, ciudad):
    """ Compara una ciudad con otra dado la hora de salida y llegada 
     Parametros
     -----------
     ciudad : City 
      ciudad a comparar
    """
    if self.hora_salida == None or ciudad.hora_salida == None:
      return self.temperatura > ciudad.temperatura
    return self.hora_salida > ciudad.hora_salida
    
  def __str__(self):
    """ Regresa la representación en cadena de una ciudad """
    return  self.nombre + " Temperatura: " + str(self.temperatura) + " °C" + " Temperatura minima: " + str(self.temp_min) + " °C" +  " Temperatura máxima: " + str(self.temp_max)  + " °C" +  " Cielo: "+ self.descripcion + " Humedad: " + str(self.humedad) + " %"
  


