# importo el modulo
import socket  

# se crea un objeto socket
Mi_socket = socket.socket()
# se indica el puerto que va a mantener a la escucha
Mi_socket.bind(("localhost", 8006))
# se le indica al socket que acepte conexiones maxima que se quiere aceptar 
Mi_socket.listen(1)  
print "Servidor arriba y escuchando!!\n"
# objeto que representa la conexion (host, puerto) del cliente 
Socket_Cliente,addr = Mi_socket.accept()  

# va a recibir numeros, hasta que el numero sea "salir" 
while True:
      # recibe el numero 
      recibido = Socket_Cliente.recv(1024)
      # si el numero es salir se sale del ciclo
      num = int(recibido)       
      #funcion pot
      def pot(x,y):
            r = x ** y
            return r
      x= pot(num,num)
      #print x
      # envia el numero al cliente 
      Socket_Cliente.send(str(x)) 
  
  

#cierro el socket cliente
Socket_Cliente.close()  
#cierro mi socket
Mi_socket.close()
