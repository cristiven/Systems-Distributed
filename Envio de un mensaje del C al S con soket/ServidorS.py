#importo el modulo del server
import SocketServer 

#creo la clase Handler
class Mi_TcpHandler(SocketServer.BaseRequestHandler):
    #se va a llamar en cada coneccion
    def handle(self):
        #recibo el mensaje
        self.msm= self.request.recv(1024).strip()
        print "El mensaje recibido es: ", self.msm
        #le mando el mensaje recibido
        self.request.send(self.msm) 
        
        
def main():
    host ="localhost" 
    port = 9999
    #creo el servidor
    Mi_server1 = SocketServer.TCPServer((host,port),Mi_TcpHandler)
    print "Servidor arriba y escuchando!!"
    #corra hasta que cierre el programa
    Mi_server1.serve_forever() 

main()
        
