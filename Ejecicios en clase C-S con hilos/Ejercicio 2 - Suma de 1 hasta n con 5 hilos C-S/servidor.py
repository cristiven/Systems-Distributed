import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading


def suma_hasta_n(x):
        #global s_t
        s = 0
        
        for i in range(x+1):
            s += i
        #s_t+=s
        return s
      
class MyThread(threading.Thread):
   
       
    def __init__(self):
        super(MyThread, self).__init__()

    def suma_hasta_n(self,x):
        #global s_t
        s = 0
        
        for i in range(x+1):
            s += i
        #s_t+=s
        return s

    
    def run(self):
        #se crea el servidor
        conexion = SimpleXMLRPCServer(("localhost",8000))
        print "Amigo soy el servidor... escuchando por el puerto: 8000 "
        conexion.register_function(self.suma_hasta_n,"suma")
		# se lanza el servidor
        conexion.serve_forever()
        #print self.suma()

	

if __name__=="__main__":
   t = MyThread()
   t.start()
   print "Hilo creado\n"

#serv = servicios()
#serv.iniciar()
        


   
