#Metodo constructor __init__

class Curso():
    #Estado inicial del objeto
    def __init__(self,nom,cre,prof):
        self.nombre = nom
        self.creditos = cre
        self.prof = prof


curso1 = Curso("Matematicas",5,"ing")
print(curso1.nombre)

curso2 = Curso("Lenguajes",4,"ing")
print(curso2.creditos)