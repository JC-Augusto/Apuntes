class coloresImagen:
    def __init__(self, x, y, booleano, color):
        self.x = x
        self.y = y
        self.booleano = booleano
        self.color = color

    def enviarData(self):
        return [self.x, self.y, self.booleano, self.color]