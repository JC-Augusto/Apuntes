class NodoMatriz:
    def __init__(self,dato,posicionX,posicionY):
        self.dato = dato

        self.arriba = None
        self.abajo = None
        self.siguiente = None
        self.anterior = None

        self.posicionX = posicionX
        self.posicionY = posicionY

class Matriz:
    def __init__(self):
        self.cabeza = None
        self.cola = None

        self.contador = 0

    def agregarX(self,dato,posicionX,posicionY):
        if self.cabeza == None:
            self.cabeza == NodoMatriz(dato,posicionX,posicionY)
        
        
