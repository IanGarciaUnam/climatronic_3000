
from AnalizadorDatos import AnalizadorDatos
import threading
analizer = AnalizadorDatos()

hilo= threading.Thread(target=analizer.emergent_advertisement)
hilo.start()
#print(analizer.ciudades_set1())
#analizer.dataSet1()
#print(analizer.get_cache())())
analizer.show_dataSet2()






