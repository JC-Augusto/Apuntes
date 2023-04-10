class Nodo:
    def __init__(self, x = None, y = None, sig = None):
        self.x = x
        self.y = y
        self.sig = sig
    
    def __str__(self):  
        return "%s %s" %(self.x, self.y)