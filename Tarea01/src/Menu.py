import time
from AnalizadorDatos import AnalizadorDatos
from Net import Net
import threading
comprobador=Net()
if comprobador.test():
	start_time = time.time()
	analizer = AnalizadorDatos()

	hilo= threading.Thread(target=analizer.emergent_advertisement)
	hilo.start()

	hilo2= threading.Thread(target=analizer.show_dataSet1)
	hilo2.start()
	
	analizer.show_dataSet2()
	print("--- %s seconds ---" % (time.time() - start_time))
else:
	print("**************RED NO DISPONIBLE, VERIFIQUE SU CONEXIÓN A INTERNET**************")










