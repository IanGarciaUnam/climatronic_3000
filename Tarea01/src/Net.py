import socket

class Net:
	""" Verificador de red 

	 Atributos
	 ----------
     tester : socket
	  verificador de red
	
	"""
	def __init__(self):
		self.tester = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def test(self):
		""" Verifica que hay red 
		 Returns
		 --------
		 True si hay, False en otro caso
		"""
		try:
			self.tester.connect(("www.google.com", 80))
			return True
		except:
			self.tester.close()
		return False

			
