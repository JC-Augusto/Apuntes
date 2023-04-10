class Token:
    '''Clase token'''
    def __init__(self, lexema, token, linea, columna):
        self.lexema = lexema
        self.token = token
        self.linea = linea
        self.columna = columna
        
    
    def imprimirData(self):
        print(self.lexema, self.token, self.linea, self.columna)

    def enviarData(self):
        return [self.lexema, self.token, self.linea, self.columna]