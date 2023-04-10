from ListaDatoxDato.Nodo import *

class LSimples:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0
    
    def agregarFin(self,elemento): 
        if self.cabeza == None:
            self.cabeza = elemento
            
    
        if self.cola != None:
            self.cola.sig = elemento
        self.cola = elemento

    def listar(self): 
        aux = self.cabeza
        while aux != None: 
            print(aux)
            aux = aux.sig

    def buscar(self,contador): 
        aux = self.cabeza
        while aux != None: 
            if contador == aux.contador:
                return aux
            aux = aux.sig 
        return None