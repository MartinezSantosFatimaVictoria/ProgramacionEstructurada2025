import mysql.connector
from mysql.connector

peliculas = []

def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n\t...Oprima cualquier tecla para continuar...") 


def crearPeliculas():
    







def mostrarPeliculas():
    borrarPantalla()
    if not peliculas:
        print("\n\tNo hay películas registradas.")
    else:
        print("\n\t.:: Listado de Películas ::.\n")
        for i, peli in enumerate(peliculas, start=1):
            print(f"\t{i}. {peli}")
    esperarTecla()

     
                



def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es:{e}")
        return None