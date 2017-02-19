import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

   
class servicios(object):
    def __init__(self,a,b):
		self.a = a
		self.b = b
    def suma_remota(self):
		return self.a + self.b
	
    def resta_remota(self):
		return self.a - self.b
		
    def mul_remota(self):
		return self.a * self.b
		
    def div_remota(self):
		return self.a / self.b

def main():
	puerto=input("Ingrese el puerto: ")
	print "Amigo soy el servidor... escuchando por el puerto "+ str(puerto)
	print "Para salir pulce Ctrl + C"
	#se crea el servidor
	conexion = SimpleXMLRPCServer(("localhost",puerto))
	serv = servicios(6,3)
	#conexion.register_function(suma_remota,"suma")
	conexion.register_instance(serv)
	# se lanza el servidor
	conexion.serve_forever()
	

main()
