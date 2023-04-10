#insertar, mostrar, insertarInicio, tamaño, buscar
#posicion, eliminarUltimo, eliminar, insertarDentro 

from cgi import print_environ_usage
import re


class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar(self,dato):
        if self.cabeza == None:
            self.cabeza = self.cola = Nodo(dato)
        else:
            temp = self.cabeza
            while temp.siguiente:
                temp = temp.siguiente
            self.cola = temp
            self.cola.siguiente = Nodo(dato)
            self.cola = self.cola.siguiente
            self.cola.anterior = temp
    
    def mostrar(self):
        temp = self.cabeza
        while temp:
            print(temp.dato, end="-->")
            temp = temp.siguiente
        print("None")
    
    def mostrarInverso(self):
        temp = self.cola
        while temp:
            print(temp.dato, end="-->")
            temp = temp.anterior
        print("None")
    
    def insertarInicio(self,dato):
        if self.cabeza == None:
            self.cabeza = self.cola = Nodo(dato)
        else:
            temp = self.cabeza
            self.cabeza = Nodo(dato)
            self.cabeza.siguiente = temp
            temp.anterior = self.cabeza
    
    def tamaño(self):
        temp = self.cabeza
        contador = 1
        while temp.siguiente:
            temp = temp.siguiente
            contador +=1
        return contador
    
    def buscar(self,dato):
        temp = self.cabeza
        while temp:
            if temp.dato == dato:
                return True
            else:
                temp = temp.siguiente
        return False
    
    def posicion(self,dato):
        temp = self.cabeza
        contador = 1
        while temp:
            if temp.dato == dato:
                return contador
            else:
                temp = temp.siguiente
                contador +=1
        return "Dato no encontrado"
    
    def eliminarUltimo(self):
        temp = self.cola
        if temp:
            if temp.anterior == None:
                self.cola = self.cabeza = None
            else:
                temp = temp.anterior
                self.cola = None
                self.cola = temp
                self.cola.siguiente = None


if __name__ == "__main__":
    lista = ListaDoble()




    lista.mostrar()


    lista.eliminarUltimo()
    lista.mostrar()
    lista.mostrarInverso()


#insertar, mostrar, insertarInicio, tamaño, buscar
#posicion, eliminarUltimo, eliminar, insertarDentro 