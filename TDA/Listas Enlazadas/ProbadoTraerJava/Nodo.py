class Nodo:
    dato = 0
    siguiente = None
    
    def Nodo(self, dato):
        """Contructor para insertar al inicio"""
        self.dato = dato

    def Nodo(self,dato,nodo):
        """Constructor para iniciaor al final"""
        self.dato = dato 
        self.siguiente = nodo
    

