from Modulos.Token import Token

class Pruebas: 
    
    def __init__(self):
        self.lista = []
        self.listaDeListas = []

    
    def agregarALista(self,lexema,token,linea,columna):
        self.lista.append(Token(lexema,token,linea,columna))

    def agregarAListaDeListas(self):
        self.listaDeListas.append(self.lista)

    def agregando(self):
        self.agregarALista("A","B","c","d")
        self.agregarALista("E","F","G","h")
        self.agregarALista("i","j","k","l")

    
    def mLista(self): 
        return self.lista
    
    def secondList(self):
        return self.listaDeListas

pr = Pruebas()

pr.agregando()
pr.agregando()

pr.agregarAListaDeListas()
pr.agregarAListaDeListas()

#print(pr.mLista()[0].enviarData())

print(pr.secondList()[1][1].enviarData())

