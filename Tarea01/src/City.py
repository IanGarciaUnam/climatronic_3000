import requests
import os
# Clase que modela una ciudad en función de temperatura
class City:
    def __init__(self, nombre, temperatura, descripcion):
        self.nombre = nombre
        self.temperatura = temperatura
        self.descripcion = descripcion

    def imprime_ciudad(self):
        d = {"Ciudad" : self.nombre, "Temperatura" : self.temperatura, "Descripción" : self.descripcion,}
        return d
    def formato(self):
      return "Pasajeros con destino a "+ self.nombre+ "se encuentra con una temperatura de "+ str(int(self.temperatura/10)) +" Grados Centigrados, Y un cielo"+ self.descripcion  
    def get_nombre():
      return str(self.nombre)
    def get_temperatura():
      return str(self.temperatura)
    def get_descripcion_clima():
      return str(self.descripcion)

