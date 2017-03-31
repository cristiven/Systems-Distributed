# importo el modulo
import socket  

#se crea un objeto socket  
Mi_socket = socket.socket()
#se conecta al servidor
Mi_socket.connect(("localhost", 8006))  
print "Ingrese el numero a calcular la potencia\n" 

#va a enviar numeros, hasta que el mensaje sea "salir"
while True:  
    num = raw_input("> ")  
    #envia el numero
    Mi_socket.send(num)
    # recibe el mensaje que le envio al servidor
    resultado_recibido = Mi_socket.recv(1024)
    print "La Potencia es: ",resultado_recibido
    # si el mensaje es salir se sale del ciclo

s.close()  
