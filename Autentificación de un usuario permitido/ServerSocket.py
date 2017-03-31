# importo el modulo
import socket

# se crea un objeto socket
Mi_socket = socket.socket()
# se indica el puerto que va a mantener a la escucha
Mi_socket.bind(("localhost", 8001))
# se le indica al socket que acepte conexiones maxima que se quiere aceptar 
Mi_socket.listen(2)  
print "Servidor arriba y escuchando!!\n"
# objeto que representa la conexion (host, puerto) del cliente 
Socket_Cliente,addr = Mi_socket.accept()  

# recibe el mensaje  
#usuario = Socket_Cliente.recv(1024)
#contrasena = Socket_Cliente.recv(1024)

def autentificacion(user, password):
      if user == "andres" and password == "123":
            r = "Hola "+ user +"," " Bienvenido al servidor"
            return r 
      else:
            e = "Lamentamos informarte que los datos de autentificacion no coinciden"
            return e

received = Socket_Cliente.recv(1024)
user, password = received.split()
print "Intento de autentificacion\n"
print "Usuario: "+user
print "Contrasena: "+password

            
x = autentificacion(user,password)
Socket_Cliente.send(str(x))

#cierro el socket cliente
Socket_Cliente.close()  
#cierro mi socket
Mi_socket.close()
