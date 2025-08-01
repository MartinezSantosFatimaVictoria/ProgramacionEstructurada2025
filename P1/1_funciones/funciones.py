"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en
 particular como un programa mas pequeño que cumple una funcion especifica. 
 La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""


#1.- Funcion que no recibe parametros y no regresa valor
def solicitarDatos1():
    nombre=input("Nombre: ")
    telefono=input("telefono: ")
    print(f"el nombre es: {nombre} y su telefono es: {telefono}")

#3.- Funcion que recibe parametros y no regresa valor
def solicitarDatos3(nom,tel):
    nombre=nom
    telefono=tel
    print(f"el nombre es: {nombre} y su telefono es: {telefono}")

# 2.- Funcion que no recibe parametros y regresa valor
def solicitarDatos2():
    nombre=input("Nombre: ")
    telefono=input("telefono: ")
    return nombre,telefono
#4.- Funcion que recibe parametros y regresa valor
def solicitarDatos4(nom,tel):
    nombre=nom
    telefono=tel
    return nombre,telefono

#invocar las funciones

solicitarDatos1()

nombre,telefono=solicitarDatos2()
print(f"\n\t\tAgenda telefonica:\n\tNombre: {nombre}\n\tTelefono{telefono}")

nombre=input("Nombre: ")
telefono=input("telefono: ")
solicitarDatos3(nombre,telefono)

nombre=input("Nombre: ")
telefono=input("telefono: ")
nombre,telefono=solicitarDatos4(nombre,telefono)
print(f"\n\t\tAgenda telefonica:\n\tNombre: {nombre}\n\tTelefono{telefono}")
