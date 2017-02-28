import thread


def imprimir_mensaje(mensaje):
	print(mensaje)
	

def main():
	mensaje = "Hola, soy un hilo"
	thread.start_new (imprimir_mensaje, (mensaje,))
	x = raw_input ("Ingresa una tecla para terminar\n")
	print ("termino la ejecucion")

main()