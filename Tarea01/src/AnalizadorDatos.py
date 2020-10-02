import os
import requests
import pandas as pd
from Voz import Voz
from City import City
class AnalizadorDatos:
    def __init__(self):
        self.ciudades_dataset1 = {
                    "MID" : "Merida", "SLP" : "San Luis Potosi", "AGU" : "Aguascalientes",
                    "CZM" : "Cozumel", "PBC" : "Puebla", "ZIH" : "Zihuatanejo", "HMO" : "Hermosillo",
                    "TAM" : "Tampico", "CTM" : "Chetumal", "GDL" : "Guadalajara", "CME" : "Ciudad del Carmen",
                    "PVR" : "Puerto Vallarta", "BJX" : "León", "CEN" : "Ciudad Obregón", "ZCL" : "Zacatecas",
                    "CUN" : "Cancún", "MZT" : "Mazatlán", "QRO" : "Querétaro", "CUU" : "Chihuahua", "MEX" : "Ciudad de México",
                    "TLC" : "Toluca", "ACA" : "Acapulco", "TRC" : "Torreón", "OAX" : "Oaxaca", "VER" : "Veracruz", 
                    "VSA" : "Villahermosa", "CJS" : "Ciudad Juárez", "MTY" : "Monterrey", "HUX" : "Huatulco", "PXM" : "Puerto Escondido",
                    }        
    
    def ciudades_set1(self):
        path = str(os.getcwd()) #Obtiene la ruta relativa en la computadora de trabajo actual

        dataset1 =  pd.read_csv(path + "/resources/dataset/dataset1.csv", names = ["origin", "destination", "origin_latitude", "origin_longitude", "destination_latitude", "destination_longitude"])
        conjunto = {}

        for i in range(1,len(dataset1["origin"])):
            conjunto[dataset1["origin"][i]] = dataset1["destination"][i]

        return conjunto
    
    def destino_llegada(self, ciudad_origen, ciudad_destino):
        return ciudad_origen.nombre + " se encuentra con una temperatura de: " + str(ciudad_origen.temperatura) + " grados centigrados y un cielo con " + ciudad_origen.descripcion +  ", mientras que " + ciudad_destino.nombre + "se encuentra con una temperatura de: " + str(ciudad_destino.temperatura) + " grados centigrados y un cielo con " + ciudad_destino.descripcion

    def dataSet1(self):

        api_adrees = 'http://api.openweathermap.org/data/2.5/weather?appid=1bfd917ba8b375efeea803bf7b9b1ee0&q=' # Llave del API para obtener info

        voice = Voz()

        for origen in self.ciudades_set1():

            aux_ciudadDestino = self.ciudades_set1()[origen]
            # Verificamos que sean vuelos solamente nacionales
            if origen in self.ciudades_dataset1 and aux_ciudadDestino in self.ciudades_dataset1:
                ciudad_origen = self.ciudades_dataset1[origen]
                ciudad_destino = self.ciudades_dataset1[aux_ciudadDestino]

                url_origen = api_adrees + ciudad_origen
                url_destino = api_adrees + ciudad_destino

                json_dataOrigen = requests.get(url_origen).json()
                json_dataDestino = requests.get(url_destino).json()

                ciudad_Origen = City(ciudad_origen, json_dataOrigen['main']['temp'], json_dataOrigen['weather'][0]['description'])
                ciudad_Destino = City(ciudad_destino, json_dataDestino['main']['temp'], json_dataDestino['weather'][0]['description'])
                print(ciudad_Origen)
                print(ciudad_Destino)
                print("--------------"*4)
                voice.into_start()
                voice.greet()
                voice.say(self.destino_llegada(ciudad_Origen, ciudad_Destino))


            
        


        
    


