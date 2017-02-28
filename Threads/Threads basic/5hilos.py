import threading
import time


class MyThread(threading.Thread):
    def __init__(self, x):
        super(MyThread, self).__init__()
        self.mensaje = x

    def run(self):
        print(self.mensaje)


if __name__ == "__main__":
    mensaje = "Hola amigos de distribuidos, soy el hilo {}"
    threads = []
    for i in range(5):
        t = MyThread(mensaje.format(i+1))
        #print "\n"
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

        


