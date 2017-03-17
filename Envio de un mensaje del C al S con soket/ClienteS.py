# importo el modulo
import socket 

host = "localhost"
port = 9999

#creo un socket y se conecta
Mi_socket= socket.socket()
Mi_socket.connect((host,port))

msm = raw_input ("Ingrese un mensaje: ")
#mando el mensaje
Mi_socket.send(msm) 

# recibo el mensaje enviado
msm_recibido = Mi_socket.recv(1024) 

print "El mensaje enviado es: ",msm_recibido

end= raw_input ("\nPresione enter para terminar...")

#cierro el socket
Mi_socket.close() 
