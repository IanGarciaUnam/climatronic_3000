import os
import time
import requests
import pandas as pd
from Voz import Voz
from City import City
from Tiempo import Tiempo
import threading
from concurrent.futures import ThreadPoolExecutor



class AnalizadorDatos:
    """ Clase para analizar los datos de los dataset 
     Atributos
     ----------
     ciudades_dataset1 : diccionario
      diccionario que contiene las ciudades del dataset1 dados sus coidgos IATA
     cache : diccionario:
      caché para evitar hacer menos peticiones
     counter : int
      contador de peticiones
    """
     
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
        self.counter = 0 # Contador de peticiones
        

    def get_ciudades(self):
        """ Regresa las ciudades del dataset1.csv """
        return self.ciudades_dataset1  
    def get_cache(self):
        """ Regresa el caché """
        return self.cache  
    def get_counter(self):
        """ Regresa el contador de peticiones """
        return self.counter

    def crea_ciudad(self, url, nombre):
        """ Crea una ciudad a partir de un request 
         Parametros
         ----------
         url : str 
          el api_adrees
         nombre : str
          nombre de la ciudad

         Returns
         ---------
         Ciudad con datos procesados
         """

        json = requests.get(url).json()
        ciudad = City(nombre, json['main']['temp'], json['weather'][0]['description'], json['main']['humidity']) 
        self.cache[nombre] = ciudad
        
        return ciudad
    
    def ciudades_set1(self):
        """ Procesa todos los vuelos del dataset1, llegada y destino. 

         Returns
         ---------
         Un conjunto de tuplas, donde cada tupla es un vuelo
        """
        path = str(os.getcwd()) #Obtiene la ruta relativa en la computadora de trabajo actual

        dataset1 =  pd.read_csv(path + "/resources/dataset/dataset1.csv", names = ["origin", "destination", "origin_latitude", "origin_longitude", "destination_latitude", "destination_longitude"]) # Abrimos el archivo csv con pandas

        conjunto = set()

         # Creamos un diccionario con los vuelos nacionales
        for i in range(1,len(dataset1["origin"])):
            tupla = (dataset1["origin"][i], dataset1["destination"][i])
            conjunto.add(tupla)

        return conjunto
    
    def ciudades_set2(self):
        """ Procesa todos los vuelos del dataset2. 

        Returns
        ---------
        Conjunto con todas las ciudades del dataset2
        """
        path = str(os.getcwd()) #Obtiene la ruta relativa en la computadora de trabajo actual

        dataset2 =  pd.read_csv(path + "/resources/dataset/dataset2.csv", names = ["destino", "salida", "llegada", "hora", "fecha de salida"])

        conjunto = set()

        # Metemos en un conjunto todas las ciudades del dataset2 
        for i in range(1,len(dataset2["destino"])):
            conjunto.add(dataset2["destino"][i])

        return conjunto
    
    def destino_llegada(self, ciudad_origen, ciudad_destino):
        """ Regresa una cadena con la infirmación de un vuelo 
         Parametros
         ----------
         ciudad_origen : City
          ciudad de origen
         ciudad_destino : City
          ciudad de destino
        
        Returns
        --------
        Una cadena que representa un vuelo
        """

        return "ORIGEN: " +str(ciudad_origen) + " >>>>>>>>>> " + "DESTINO: "+ str(ciudad_destino) + "\n" 
    

    def verifica_cacheSet1(self, api_adrees, ciudad1, ciudad2):
        """ Verifica e imprime la información del dataset1 
         Parametros
         ----------
         api_adrees : str
          el api_adrees
         ciudad1 : str
          ciudad de origen
         ciudad2 : str
          ciudad de destino
        """
       
        ciudad_origen = self.ciudades_dataset1[ciudad1]
        ciudad_destino = self.ciudades_dataset1[ciudad2]
        if ciudad_origen in self.cache and ciudad_destino in self.cache: # Checamos si están en el caché
            ciudad_Origen = self.cache[ciudad_origen]
            ciudad_Destino = self.cache[ciudad_destino] 

        elif ciudad_origen in self.cache and ciudad_destino not in self.cache:
            ciudad_Origen = self.cache[ciudad_origen]
            ciudad_Destino = self.crea_ciudad(api_adrees + ciudad_destino, ciudad_destino)
            self.counter += 1
        elif ciudad_origen not in self.cache and ciudad_destino in self.cache:
            ciudad_Destino = self.cache[ciudad_destino] 
            ciudad_Origen = self.crea_ciudad(api_adrees + ciudad_origen, ciudad_origen)
            self.counter += 1

        else:
            if self.counter >= 21:
                self.counter = 1
                time.sleep(10)

            ciudad_Origen = self.crea_ciudad(api_adrees + ciudad_origen, ciudad_origen)
            ciudad_Destino = self.crea_ciudad(api_adrees + ciudad_destino, ciudad_destino) 
            self.counter += 2
        print(self.cache)
        print("*******************************************************************************************************************")
        print(self.destino_llegada(ciudad_Origen,ciudad_Destino))
        print("*******************************************************************************************************************" + "\n")

    def show_dataSet1(self):
        """ Procesa los datos del dataset1 y nos regresa la información deseada """

        start_time = time.time()
        api_adrees = 'http://api.openweathermap.org/data/2.5/weather?appid=1bfd917ba8b375efeea803bf7b9b1ee0&q=' # Llave del API para obtener info
        pool = ThreadPoolExecutor(max_workers=15)
        session = requests.Session()
        with pool:
            with session:
                for tupla in self.ciudades_set1():
                    future = pool.submit(self.verifica_cacheSet1, api_adrees, tupla[0], tupla[1])

        print(self.get_counter())

        print("--- %s seconds ---" % (time.time() - start_time))

    def verifica_cacheSet2(self, api_adrees, s):
        """ Procesa e imprime la información de una ciudad del dataset2 
         Parametros
         ----------
         api_adrees : str
          el api_adrees
         s : str
          la ciudad a procesar
        """
        if s in self.cache:
            ciudad = self.cache[s]
        else:
            if self.counter >= 31:#Solo tomamos 30 peticiones para poder tomar 29 de nuestro dataset1
                self.counter = 1 
                time.sleep(60)
            self.counter += 1
            url = api_adrees + s
            json_data = requests.get(url).json()
            if json_data != {"cod":"404","message":"city not found"}:
                ciudad = City(s, json_data['main']['temp'], json_data['weather'][0]['description'], json_data['main']['humidity'])
                self.cache[s] = ciudad
            print("********************************************************************************")
            print("\t"+ str(ciudad))
            print("********************************************************************************")

        

    def show_dataSet2(self):
        """ Procesa los datos del dataset2 y nos regresa la información deseada """
        start_time = time.time()
        api_adrees = 'http://api.openweathermap.org/data/2.5/weather?appid=1bfd917ba8b375efeea803bf7b9b1ee0&q=' # Llave del API para obtener info
        pool = ThreadPoolExecutor(max_workers=10)
        session = requests.Session()
        with pool:
            with session:
                for s in self.ciudades_set2():
                    future = pool.submit(self.verifica_cacheSet2, api_adrees, s)
        print("--- %s seconds ---" % (time.time() - start_time))
            



    def emergent_advertisement(self):
        """ Función auxliar para ordenar las ciudades por hora de salida y repetir a voz """
        start_time = time.time()
        path = str(os.getcwd()) #Obtiene la ruta relativa en la computadora de trabajo actual

        dataset2 =  pd.read_csv(path + "/resources/dataset/dataset2.csv", names = ["destino", "salida", "llegada", "hora", "fecha de salida"])
        lista_ciudades=[]


        #Esta es una función auxiliar, permite generar avisos audiovisuales para los vuelos próximos a salir
        api_adrees = 'http://api.openweathermap.org/data/2.5/weather?appid=1bfd917ba8b375efeea803bf7b9b1ee0&q=' # Llave del API para obtener info
        contador_externo=1
        for i in range(1,len(dataset2["destino"])):
            ciudad=None
            if contador_externo%11==0:
                contador_externo=1
                time.sleep(11)

            if dataset2["destino"][i] in self.cache:

                ciudad = self.cache[dataset2["destino"][i]]
                contador_externo-=1
            else:
                url=api_adrees + dataset2["destino"][i]
                json_data = requests.get(url).json()
                if json_data == {"cod": "404", "message" : "city not found"}:
                    continue
                ciudad = City(dataset2["destino"][i], json_data['main']['temp'], json_data['weather'][0]['description'], json_data['main']['humidity'])
                contador_externo+=1
            try:
                #print(dataset2["salida"][i])
                ciudad.set_hora_salida(dataset2["salida"][i])
                #print(str(ciudad)+" de hilo")
            except Exception:
                continue
            lista_ciudades.append(ciudad)
            print(ciudad)
            
            if len(lista_ciudades) == 20:
                lista_ciudades.sort()
                for ciudad in lista_ciudades:
                    i+=5
                    self.advertisement(ciudad.formato(), ciudad.formato_salida())
                lista_ciudades.clear()
        print("--- %s seconds ---" % (time.time() - start_time))


    def advertisement(self,cadena_formato, formato_salida):
        """ Imprime la información de una ciudad """
        print("==========================================================================================================")
        print("\t\t" + str(cadena_formato))
        print("==========================================================================================================")
        voice= Voz()
        voice.into_start()
        voice.greet()
        voice.say(formato_salida)
        time.sleep(15) #Desajustamos sumando 77 sec a los 11 dados tras 11 10 request







            
        


        
    


