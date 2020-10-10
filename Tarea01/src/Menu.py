import time
from AnalizadorDatos import AnalizadorDatos
from Net import Net
import threading

comprobador=Net()
def main():
	if comprobador.test():
		analizer = AnalizadorDatos()
		hilo1= threading.Thread(target=analizer.show_dataSet1)
		time.sleep(20)
		hilo2 = threading.Thread(target=analizer.show_dataSet2)
		hilo3= threading.Thread(target=analizer.emergent_advertisement)
		hilo3.start()
		hilo2.start()
		hilo1.start()

		hilo1.join()
		hilo2.join()
		hilo3.join()



	else:
		print("**************RED NO DISPONIBLE, VERIFIQUE SU CONEXIÓN A INTERNET**************")

if __name__ == "__main__":
    main()










