import xmlrpclib
print "Amigo soy el cliente... estas son tus funciones \n"

#x=input('ingrese el primer numero: ')
#y=input('ingrese el segundo numero: ')

#creando la conexion
proxy=xmlrpclib.ServerProxy("http://localhost:8000/")
print "la suma es: " + str(proxy.suma_remota())
print "la resta es: " + str(proxy.resta_remota())
print "la multiplicacion es: " + str(proxy.mul_remota())
print "la division: " + str(proxy.div_remota())
