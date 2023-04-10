class Nodo:
    def __init__(self, nombre = None, cedula = None, ant = None,sig = None):
        self.nombre = nombre 
        self.cedula = cedula
        self.sig = sig
    
    def __str__(self):  
        return "%s %s" %(self.nombre, self.cedula)
    