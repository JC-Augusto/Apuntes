class datosImagen():

    def __init__(self,titulo,ancho,alto,filas,columna):
        self.titulo = titulo
        self.ancho = ancho
        self.alto = alto
        self.filas = filas
        self.columna = columna
    
    def enviarData(self):
        return [self.titulo, self.ancho, self.alto, self.filas, self.columna]