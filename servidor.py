from SimpleXMLRPCServer import SimpleXMLRPCServer as Server
import xmlrpclib


def factorial(n):
		if n==0:
			return 1
		else:
			return factorial(n-1)*n
		    
def crear_archivo(dato):
	archivo = "Respuesta_servidor_Datos_lista.txt"
	arch = open(archivo,'w+') 
	for a in dato:
		arch.write(str(a)+"\n")
	
	arch.close()
	return archivo



class Operaciones:
    def potencia(self,x,y):
        if y==0:
            return 1
        else:
            return self.potencia(x,y-1)*x
    def factorial(self,n):
        if n==0:
            return 1
        else:
            return self.factorial(n-1)*n
        
    def fibonacci(self,n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fibonacci(n-1)+self.fibonacci(n-2)

    # Recibe el archivo de texto del cliente
    #def receive_data(self,nom_arch):
        #with open(nom_arch, "rb") as handle:
            #return xmlrpclib.Binary(handle.read())
    def server_receive_file(self,arg):
        with open("C:\Users\Estudiantes\Downloads\Funcionando localhost\Datos_Recibidos_Cliente.txt", "wb") as handle:
            handle.write(arg.data)
            return True

    def calcular_datos(self,nom_arch):
        file = open(nom_arch,'r')
        li = []
        for num in file:
                f=factorial(int(num))
                li.append(f)
        file.close
        crear_archivo(li)
        return li
    
    #def llamado_calcular(self):
        #r=calcular_datos("Respuesta_servidor_Datos_lista.txt")
        #return r

conexion = Server(("192.168.9.82", 8000))
print "###################servidor ONLINE #####################################"
print "Soy el servidor y estoy escuchando por el puerto:" + str(8000)
conexion.register_instance(Operaciones())
conexion.serve_forever()
