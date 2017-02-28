import threading
import time

s_t=0
class MyThread(threading.Thread):
    
    def __init__(self, x, y):
        super(MyThread, self).__init__()
        self.x = x
        self.y = y
        
    def suma(self):
        global s_t
        s = 0
        for i in range(self.x,self.y):
            s += i
        s_t+=s
        return s
        
    def run(self):
        print self.suma()
         

    
if __name__ == "__main__":
    threads = []
    tam = 100 / 5
    for i in range(5):
        start = i * tam + 1
        end = start + tam
        t = MyThread(start,end)
        print "\n"
        print "Hilo {0}: Suma de {1} al {2}".format(i+1,start,end)
        t.start()
        threads.append(t)

        
    for t in threads:
        t.join()
    
    print ("\nLa suma total es: "+str(s_t))

    

        


