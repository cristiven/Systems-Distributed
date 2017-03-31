# importo el modulo
import socket
import getpass

#se crea un objeto socket  
Mi_socket = socket.socket()
#se conecta al servidor
Mi_socket.connect(("localhost", 8001))  


usuario = raw_input("Ingrese su nombre de usuario: ")
password = getpass.getpass()
send_data = usuario +" " + password

# envia varios datos
Mi_socket.sendall(send_data)


# recibe la notificacion del servidor
rec_notificacion = Mi_socket.recv(1024)
print rec_notificacion

       
# cierro el socket  
Mi_socket.close()  
