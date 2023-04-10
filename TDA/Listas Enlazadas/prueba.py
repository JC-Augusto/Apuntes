from SimplementeEnlazada.Lista import * 
from SimplementeEnlazada.Nodo import *

if __name__ == "__main__":
    ls = LSimples()
    while(True):
        print("""MENU
        1. Agregar
        2. Listar""")

        num = int(input("Ingrese una opcion: "))
        if num == 1:
            nombre = input("Ingrese el nombre: ")
            cedula = input("Ingrese la cedula: ")
            nod = Nodo(nombre,cedula)
            ls.agregarFin(nod)
        elif num == 2:
            ls.listar()
    
