class Nodo:
    def __init__(self, dato = None, contador = None, sig = None):
        self.contador = contador
        self.dato = dato
        self.sig = sig
    
    def __str__(self):  
        return "%s" %(self.dato)
    