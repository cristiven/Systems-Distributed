import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

def suma_remota(a,b):
   return a+b

def resta_remota(a,b):
   return a-b
   
class servicios:
    def __init__(self):
        pass
    #def suma_remota(self,a,b):
    #    return a+b
    def iniciar(self):
        puerto=input("ingrese el puerto: ")
        #se crea el servidor
        conexion = SimpleXMLRPCServer(("localhost",puerto))
        print "Amigo soy el servidor... escuchando por el puerto "+ str(puerto)
        conexion.register_function(suma_remota,"suma")
		# se lanza el servidor
        conexion.serve_forever()
	

serv = servicios()
serv.iniciar()
