from SimplementeEnlazada.Nodo import *

class LSimples:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
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


