#Creacion de una clase sin constructor

class Persona():
    #Propiedades, caracteristicas o atributos
    appellidos = ""
    nombres = ""
    edad = 0
    despierta = False

    #funcionalidades
    def despertar(self):
        # self: Parametro que hace referencia a la instancia perteneciente a la clase
        self.despierta = True
        print("buen dia!")

persona1 = Persona()
persona1.appellidos = "Garcia Fuentes"
print(persona1.appellidos)
persona1.despertar()
print(persona1.despierta)

persona2 = Persona()
persona2.appellidos = "Paz Torres"
print(persona2.appellidos)
print(persona2.despierta)