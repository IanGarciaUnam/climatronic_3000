import os
import time
import requests
import pandas as pd
from Voz import Voz
from City import City
from Tiempo import Tiempo
import threading



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
                    "PHL" : "Filadelfia", "HAV" : "La Habana", "CLT" : "Charlotte", "YVR" : "Vancouver", "MAD" : "Madrid", "DFW" : "Dallas",
                    "YYZ" : "Toronto", "LAX" : "Los Ángeles", "SCL" : "Santiago", "ORD" : "Chicago", "PHX" : "Phoenix" , "BOG" : "Bogotá",
                    "MIA" : "Miami", "IAH" : "Houston", "BZE" : "Belice", "ATL" : "Atlanta", "LIM" : "Lima", "JFK" : "Nueva York",
                    "GUA" : "Guatemala", "CDG" : "Paris", "AMS" : "Amsterdam", "TIJ" : "Tijuana"
                    }   
        self.cache = {} # Caché para evitar hacer más requests de las necesarias
        

    def get_ciudades(self):
        """ Regresa las ciudades del dataset1.csv """
        return self.ciudades_dataset1  
    def get_cache(self):
        """ Regresa el caché """
        return self.cache  
    
    def ciudades_set1(self):
        """ Procesa todos los vuelos del dataset1, llegada y destino. """
        path = str(os.getcwd()) #Obtiene la ruta relativa en la computadora de trabajo actual

        dataset1 =  pd.read_csv(path + "/resources/dataset/dataset1.csv", names = ["origin", "destination", "origin_latitude", "origin_longitude", "destination_latitude", "destination_longitude"]) # Abrimos el archivo csv con pandas

        conjunto = {}

         # Creamos un diccionario con los vuelos nacionales
        for i in range(1,len(dataset1["origin"])):
            conjunto[dataset1["origin"][i]] = dataset1["destination"][i]

        return conjunto
    
    def ciudades_set2(self):
        """ Procesa todos los vuelos del dataset2. """
        path = str(os.getcwd()) #Obtiene la ruta relativa en la computadora de trabajo actual

        dataset2 =  pd.read_csv(path + "/resources/dataset/dataset2.csv", names = ["destino", "salida", "llegada", "hora", "fecha de salida"])

        conjunto = set()

        # Metemos en un conjunto todas las ciudades del dataset2 
        for i in range(1,len(dataset2["destino"])):
            conjunto.add(dataset2["destino"][i])

        return conjunto
    
    def destino_llegada(self, ciudad_origen, ciudad_destino):
        # Esto va a ser función de Voz
        return ciudad_origen.nombre + " se encuentra con una temperatura de: " + str(ciudad_origen.temperatura) + " grados centigrados y un cielo con " + ciudad_origen.descripcion +  ", mientras que " + ciudad_destino.nombre + "se encuentra con una temperatura de: " + str(ciudad_destino.temperatura) + " grados centigrados y  con " + ciudad_destino.descripcion

    def dataSet1(self):
        """ Procesa los datos del dataset1 y nos regresa la información deseada """
        start_time = time.time()
        api_adrees = 'http://api.openweathermap.org/data/2.5/weather?appid=1bfd917ba8b375efeea803bf7b9b1ee0&q=' # Llave del API para obtener info

        for origen in self.ciudades_set1():

            aux_ciudadDestino = self.ciudades_set1()[origen]
            ciudad_origen = self.ciudades_dataset1[origen]
            ciudad_destino = self.ciudades_dataset1[aux_ciudadDestino]
            if ciudad_origen in self.cache and ciudad_destino in self.cache: # Checamos si están en el caché
                ciudad_Origen = self.cache[ciudad_origen]
                ciudad_Destino = self.cache[ciudad_destino]
            else:
                url_origen = api_adrees + ciudad_origen
                url_destino = api_adrees + ciudad_destino

                json_dataOrigen = requests.get(url_origen).json()
                json_dataDestino = requests.get(url_destino).json()

                ciudad_Origen = City(ciudad_origen, json_dataOrigen['main']['temp'], json_dataOrigen['weather'][0]['description'])
                ciudad_Destino = City(ciudad_destino, json_dataDestino['main']['temp'], json_dataDestino['weather'][0]['description']) 
                
            self.cache[ciudad_origen] = ciudad_Origen
            self.cache[ciudad_destino] = ciudad_Destino
            

        print("--- %s seconds ---" % (time.time() - start_time))

    def show_dataSet2(self):
        """ Procesa los datos del dataset2 y nos regresa la información deseada """

        api_adrees = 'http://api.openweathermap.org/data/2.5/weather?appid=1bfd917ba8b375efeea803bf7b9b1ee0&q=' # Llave del API para obtener info
        start_time = time.time()
        counter=1
        for s in self.ciudades_set2():
            time.sleep(0.2)#Ayuda en la generación de un delay
            if s in self.cache:
                ciudad = self.cache[s]
            else:
                if counter%30==0: #Solo tomamos 30 peticiones para poder tomar 29 de nuestro dataset1
                    time.sleep(60)
                counter+=1
                url = api_adrees + s
                json_data = requests.get(url).json()
                if json_data == {"cod":"404","message":"city not found"}:
                    continue

                ciudad = City(s, json_data['main']['temp'], json_data['weather'][0]['description'])
            self.cache[s] = ciudad

            print("\t"+ str(ciudad))

        print("--- %s seconds ---" % (time.time() - start_time))


    def emergent_advertisement(self):
        print("doing")
        """ Función auxliar para ordenar las ciudades por hora de salida y repetir a voz """
        path = str(os.getcwd()) #Obtiene la ruta relativa en la computadora de trabajo actual

        dataset2 =  pd.read_csv(path + "/resources/dataset/dataset2.csv", names = ["destino", "salida", "llegada", "hora", "fecha de salida"])
        lista_ciudades=[]


        #Esta es una función auxiliar, permite generar avisos audiovisuales para los vuelos próximos a salir
        api_adrees = 'http://api.openweathermap.org/data/2.5/weather?appid=1bfd917ba8b375efeea803bf7b9b1ee0&q=' # Llave del API para obtener info
        contador_externo=1
        for i in range(1,len(dataset2["destino"])):
            ciudad=None
            if contador_externo==11==0:
                contador_externo=1
                time.sleep(52)

            if dataset2["destino"][i] in self.cache:

                ciudad = self.cache[dataset2["destino"][i]]
                contador_externo-=1
            else:
                url=api_adrees + dataset2["destino"][i]
                json_data = requests.get(url).json()
                if json_data == {"cod": "404", "message" : "city not found"}:
                    continue
                ciudad = City(dataset2["destino"][i], json_data['main']['temp'], json_data['weather'][0]['description'])
                contador_externo+=1
            try:
                #print(dataset2["salida"][i])
                ciudad.set_hora_salida(dataset2["salida"][i])
                print(str(ciudad)+" de hilo")
            except Exception:
                continue
            lista_ciudades.append(ciudad)
            print(ciudad)
            
            if len(lista_ciudades)==5:
                lista_ciudades.sort()
                for ciudad in lista_ciudades:
                    self.advertisement(ciudad.formato(), ciudad.formato_salida())
                lista_ciudades.clear()


    def advertisement(self,cadena_formato, formato_salida):
        print("==========================================================================================================")
        print("\t\t" + str(cadena_formato))
        print("==========================================================================================================")
        voice= Voz()
        voice.into_start()
        voice.greet()
        voice.say(formato_salida)
        time.sleep(100)







            
        


        
    


