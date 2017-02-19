import xmlrpclib
import os
import time

def crear_archivo(dato):
	archivo = "Datos_lista.txt"
	arch = open(archivo,'w+') 
	for a in dato:
		arch.write(str(a)+"\n")
	
	arch.close()
	return archivo

def menu():
  print "##############BIENVENIDOS AL MENU ARITMETICO#####################"
  print "     1. POTENCIA"
  print "     2. FACTORIAL"
  print "     3. SERIE DE FIBONACCI"
  print "     4. LLENAR LISTA/TUPLA"
  print "     0. PARA SALIR"

def conectar():
  menu()
  a = input('Ingrese una opcion: ')
  if a == 1:
    os.system('clear')
    b = input('Ingrese la base: ')
    c = input('Ingrese el exponente: ')
    print "El valor de la potencia es : "+str(proxy.potencia(b,c))

  elif a == 2:
    os.system('clear')
    n=input("ingrese un entero: ")
    print "el factorial de : "+str(n)+str(" es: ")+str(proxy.factorial(n))

  elif a == 3:
    os.system('clear')
    n = input("ingrese un entero: ")
    print "el numero de fibonacci es: "+str(proxy.fibonacci(n))

  elif a == 4:
    os.system('clear')
    li = raw_input("Ingrese los numeros de la lista: ")
    li = li.rstrip() 
    nom_arch = crear_archivo(li) 
    print "Archivo creado con el nombre: "+nom_arch
    time.sleep( 3 )
    print "Enviando archivo al servidor..."
    time.sleep( 3 )
    print "Archivo generado por el servidor.\n"
    time.sleep( 1 )
    print "El factorial de cada elemento de tu lista es: "+str(proxy.get_file(nom_arch))

    
    
    # Envia el archivo de texto al servidor
    with open("Enviando_"+nom_arch, "wb") as handle:
                    handle.write(proxy.receive_data(nom_arch).data)
                    
  elif a == 0:
      print "Para el servidor y todo el equipo fue un placer atenderle, regresa pronto a nuestro MENU"
      exit()


proxy = xmlrpclib.ServerProxy('http://localhost:8000/')
conectar()
