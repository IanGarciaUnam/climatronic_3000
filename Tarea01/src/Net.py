import socket

class Net:
	"""docstring for Net"""
	def __init__(self):
		self.tester=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def  test(self):
		try:
			self.tester.connect(("www.google.com", 80))
			return True
		except:
			self.tester.close()
		return False

			
