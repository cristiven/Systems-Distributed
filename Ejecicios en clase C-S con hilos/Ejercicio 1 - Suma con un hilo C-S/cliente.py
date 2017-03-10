import xmlrpclib
print "Amigo soy el cliente \n"

x=input('ingrese el primer numero: ')
y=input('ingrese el segundo numero: ')

#creando la conexion
proxy=xmlrpclib.ServerProxy("http://localhost:8000/")
print "la suma es: " + str(proxy.suma(x,y))


