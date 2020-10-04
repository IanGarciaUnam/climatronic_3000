from AnalizadorDatos import AnalizadorDatos
import os

analizer = AnalizadorDatos()

path = str(os.getcwd()) #Obtiene la ruta relativa en la computadora de trabajo actual
cont = 0
archivo = open(path + "/results.txt", "r")
for x in archivo:
    if x.strip().rstrip("\n") not in analizer.get_ciudades():
        print("There is key values missing")
        break

print("Test")


