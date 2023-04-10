class Nodo:
    def __init__(self, dato, sig = None):
        self.dato = dato
        self.sig = sig
    
    def __str__(self):  
        return "%s" %(self.dato)