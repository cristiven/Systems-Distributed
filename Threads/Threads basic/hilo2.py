from threading import Thread

class MiHilo(Thread):
   def suma(self,a,b):
	return a+b
   def run(self):
	print("hola Amigo, yo soy un Hilo")
	print("aparte de imprimir un mensaje, tambien puedo hacer otras cosas:")
	print "por ejemplo la suma de 2+3 es: "+str(self.suma(2,3))
hilo = MiHilo()
hilo.start()
