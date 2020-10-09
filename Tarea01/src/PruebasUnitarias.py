from AnalizadorDatos import AnalizadorDatos
from City import City
from Tiempo import Tiempo
from datetime import datetime
import unittest
import random
import requests
import socket
from Net import Net

class PruebasUnitarias(unittest.TestCase):
    """ Clase para para pruebas unitarias """
    def prueba_internet(self):
        tester = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            tester.connect(("www.facebook.com", 80))
            return True
        except:
            tester.close()
        return False

    def test_red(self):
        """ Prueba para verificar el Verificador de conexión a internet"""
        n=Net()

        self.assertEqual(self.prueba_internet(), n.test())
    
    def test_ciudadString(self):
        """ Prueba unitaria para verificar que __str__ de una ciudad funciona correctamente """
        ciudad= City("CDMX", 30, "nublado", 30, 12, 25)
        self.assertEqual(ciudad.__str__() , ciudad.get_nombre() + " Temperatura: " + ciudad.get_temperatura() + " °C" + " Temperatura minima: " + ciudad.get_temp_min() + " °C" +  " Temperatura máxima: " + ciudad.get_temp_max()  + " °C" +  " Cielo: "+ ciudad.get_descripcion_clima() + " Humedad: " + ciudad.get_humedad() + " %")
    
    def test_string_hora(self):
        """ Prueba unitaria para convertir un string a hora"""
        my_string="Hola que hace"
        t=Tiempo()
        try:
            h=t.convert_into_hour(my_string)
        except ValueError:
            print("Accepted")

        self.assertEqual(datetime.strptime("12:23", '%H:%M'),t.convert_into_hour("12:23"))





if __name__ == '__main__': 
    unittest.main() 