import socket
import threading
import sys

  
class Cliente():
	
	def __init__(self, host="localhost", port=8000):
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))

		msg_recv = threading.Thread(target=self.msg_recv)

		#para que el hilo se muera y no quede como un proceso
		msg_recv.daemon = True
		msg_recv.start()
		
		print "     ########     Bienvenido al Chat !!!!!     #######\n"
		
		user = raw_input('Ingrese su nombre: ')
		print "\nIngrese un mensaje o 'salir' para terminar\n"

		while True:
                        msg = raw_input('>')
			print "\n"
			if msg != 'salir':
				data = user + "\n" + msg + "\n"  
				self.send_msg(data)
			else:
				self.sock.close()
				sys.exit()

	def msg_recv(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print data
					
					

			except:
				pass

	def send_msg(self, msg):
		self.sock.sendall(msg)
		


c = Cliente()
		
