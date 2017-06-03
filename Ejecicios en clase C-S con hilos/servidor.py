import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading


#def suma_remota(a,b):
   #return a+b

class MyThread(threading.Thread):
   
    def __init__(self):
        super(MyThread, self).__init__()

    def suma_remota(self,x,y):
       return x + y
        
    def run(self):
        #se crea el servidor
        conexion = SimpleXMLRPCServer(("localhost",8000))
        print "Amigo soy el servidor... escuchando por el puerto: 8000 "
        conexion.register_function(self.suma_remota,"suma")
		# se lanza el servidor
        conexion.serve_forever()
	

if __name__=="__main__":
   t = MyThread()
   t.start()
   print "Hilo creado\n"

#serv = servicios()
#serv.iniciar()
