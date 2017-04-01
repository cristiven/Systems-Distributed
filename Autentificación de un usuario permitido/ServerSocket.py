# importo el modulo
import socket

# se crea un objeto socket
Mi_socket = socket.socket()
# se indica el puerto que va a mantener a la escucha
Mi_socket.bind(("localhost", 8006))
# se le indica al socket que acepte conexiones maxima que se quiere aceptar 
Mi_socket.listen(2)  
print "Servidor arriba y escuchando!!\n"
# objeto que representa la conexion (host, puerto) del cliente 
#Socket_Cliente,addr = Mi_socket.accept()  

# recibe el mensaje  
# usuario = Socket_Cliente.recv(1024)
# contrasena = Socket_Cliente.recv(1024)

def autentificacion(user, password):
      if user == "stiven" and password == "123":
            return True 
      else:
            return False

while True:
      Socket_Cliente,addr = Mi_socket.accept()
      try:
           received = Socket_Cliente.recv(1024)
           user, password = received.split()
           print "Intento de autentificacion\n"
           print "Usuario: "+user
           print "Contrasena: "+password
           x = autentificacion(user,password)
           Socket_Cliente.send(str(x))
      except:
            #cierro el socket cliente
            Socket_Cliente.close()  
            #cierro mi socket
            Mi_socket.close()
