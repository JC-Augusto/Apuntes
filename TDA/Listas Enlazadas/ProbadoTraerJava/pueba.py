from ProbadoTraerJava.Lista import * 
from ProbadoTraerJava.Nodo import *

menu = 0
lista = Lista()
while menu != 4: 
    print("""Ingrese las opciones que quiera:
    1. agregar
    2. listar
    3. nada
    4. salir
    """)
    menu = input("ingresea tu opcion: ")

    if menu == 1: 
        elemento = input("ingrese un elemento: ")
        lista.agregarInicio(elemento)
    elif menu == 2: 
        pass
