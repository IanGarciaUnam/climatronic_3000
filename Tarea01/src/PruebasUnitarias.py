from AnalizadorDatos import AnalizadorDatos
from City import City
import unittest
import random
import requests
analizer = AnalizadorDatos()
class PrubasUnitarias(unittest.TestCase):
    """ Clase para para pruebas unitarias """
    def test_cacheSet1(self):
        """ Pruba unitaria para verfiicar que el caché después de procesar el dataset1 contenga el mismo de número de ciudades que hay en el dataset1 """
        analizer.show_dataSet1()
        self.assertEquals(len(analizer.get_cache()), len(analizer.get_ciudades()))
    
    def test_ciudadString(self):
        """ Prueba unitaria para verificar que __str__ de una ciudad funciona correctamente """
        conjunto = analizer.ciudades_set2()
        lista = []
        for e in conjunto:
            lista.append(e) 
        
        ciudad = random.choice(lista)
        url = 'http://api.openweathermap.org/data/2.5/weather?appid=1bfd917ba8b375efeea803bf7b9b1ee0&q=' + ciudad

        city = analizer.crea_ciudad(url, ciudad)

        self.assertEqual(city.__str__() , city.get_nombre() + " Temperatura: " + city.get_temperatura()+ " °C"+ " Cielo: " + city.get_descripcion_clima() + " Humedad: " + ciudad.get_humedad())
    
    def test_requests(self):
        """ Prueba unitaria para ver que una ciudad existe en el dataset2 """
        conjunto = analizer.ciudades_set2()
        lista = []
        for e in conjunto:
            lista.append(e) 

        ciudad = random.choice(lista)
        url = 'http://api.openweathermap.org/data/2.5/weather?appid=1bfd917ba8b375efeea803bf7b9b1ee0&q=' + ciudad

        json = requests.get(url).json()

        self.assertNotEqual(json, {"cod":"404","message":"city not found"})




if __name__ == '__main__': 
    unittest.main() 