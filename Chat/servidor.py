import socket
import threading
import sys


class Servidor():
	
	def __init__(self, host="localhost", port=8000):

		self.clientes = []

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((str(host), int(port)))
		self.sock.listen(10)
		self.sock.setblocking(False)

		aceptar = threading.Thread(target=self.accept_connection)
		procesar = threading.Thread(target=self.process_connection)

		#para que el hilo se muera y no quede como un proceso
		aceptar.daemon = True
		aceptar.start()

		procesar.daemon = True
		procesar.start()
		
		while True:
			print "\n"
			msg = raw_input('Ingrese salir si desea terminar: ')
			if msg == 'salir':
				self.sock.close()
				sys.exit()
			else:
				pass


	def msg_to_all(self, msg, cliente):
		for c in self.clientes:
			try:
				if c != cliente:
					c.send(msg)
			except:
				self.clientes.remove(c)

	def accept_connection(self):
		print("Servidor arriba y escuchando... !!!\n")
		i = 0
		while True:
			try:
				conn, addr = self.sock.accept()
				print "\nSe ha conectado el cliente {0} {1}\n".format(i+1,addr)
				conn.setblocking(False)
				self.clientes.append(conn)
				i=i+1
			except:
				pass
		

	def process_connection(self):
		print("Conexion iniciada")
		
		while True:
			if len(self.clientes) > 0:
				for c in self.clientes:
					try:
						data = c.recv(1024)
						if data:
							self.msg_to_all(data,c)
					except:
						pass


s = Servidor()
