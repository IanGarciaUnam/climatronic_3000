
from AnalizadorDatos import AnalizadorDatos
from Net import Net
import threading

comprobador=Net()
if comprobador.test():
	analizer = AnalizadorDatos()
	hilo= threading.Thread(target=analizer.emergent_advertisement)
	hilo.start()
	hilo= threading.Thread(target=analizer.show_dataSet1)
	hilo.start()
	analizer.show_dataSet2()
else:
	print("**************RED NO DISPONIBLE, VERIFIQUE SU CONEXIÓN A INTERNET**************")










