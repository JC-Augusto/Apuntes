class Curso(): 

    def __init__(self,nombre,creditos, profesion):
        self.nombre = nombre
        self.creditos = creditos
        self.curso = profesion
        self.__imparticion = "Presencial" #Propiedad encapsulada

    def mostrarDatos(self):
        dat = "Nombre: {0} / Creditos: {1} / Modo de impartición: {2}"
        print(dat.format(self.nombre, self.creditos, self.__imparticion))

curso1 = Curso("Matemática",5,"Ingenieria")
curso1.mostrarDatos()
print(curso1.nombre)
print(curso1.__imparticion)