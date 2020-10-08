import time
from AnalizadorDatos import AnalizadorDatos
from Net import Net
import threading
comprobador=Net()
if comprobador.test():
	analizer = AnalizadorDatos()


	print("***** VUELOS DEL DATASET1 *******")
	analizer.show_dataSet1()
	print("****** FINAL DE LOS VUELOS DEL DATASET1 *********")
	time.sleep(20)

	print("******* VUELOS DEL DATASET2 *************")
	analizer.show_dataSet2()
	print("****** FINAL DE LOS VUELOS DEL DATASET1 *********")


else:
	print("**************RED NO DISPONIBLE, VERIFIQUE SU CONEXIÓN A INTERNET**************")










