from ProbadoTraerJava.Nodo import *

class Lista:
    #Punteros tipo nodo para saber donde esta el inicio y el fin

    inicio = None 
    fin = None 

    def Lista(self):
        self.inicio = None
        self.fin = None
    
    def agregarInicio(self,elemento):
        self.inicio = Nodo(elemento,self.inicio)
        if self.fin == self.inicio:
            self.fin = self.inicio

    def mostrarLista(self):
        recorrer = self.inicio
        while (recorrer != None):
            print("["+recorrer.dato+"]")
            recorrer = recorrer.siguiente


