class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar(self,dato):
        if self.cabeza == None:
            self.cabeza = Nodo(dato)
        else:
            temp = self.cabeza
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = Nodo(dato)
    
    def insertarInicio(self,dato):
        if self.cabeza == None:
            self.cabeza = Nodo(dato)
        else:
            temp = self.cabeza
            self.cabeza = Nodo(dato)
            self.cabeza.siguiente = temp

    def tamaño(self) -> int:
        temp = self.cabeza
        contador = 0
        while temp:
            temp = temp.siguiente
            contador +=1
        return contador

    def mostrar(self):
        temp = self.cabeza
        while temp:
            print(temp.dato, end="-->")
            temp = temp.siguiente
        print("Null")

    def buscar(self,dato):
        temp = self.cabeza
        while temp:
            if temp.dato == dato:
                return "El dato: "+ str(dato) + " si se encuentra en la lista en la posicion: " +str(self.posicion(dato))
            temp = temp.siguiente
        return "Dato no encontrado"

    def posicion(self,dato):
        temp = self.cabeza
        contador = 1
        while temp:
            if temp.dato == dato:
                return contador
            temp = temp.siguiente
            contador +=1

    def eliminar(self,index):
        if int(index) > int(self.tamaño()):
            print("el valor buscado no existe")
        else:
            temp = self.cabeza
            contador = 1
            while contador != int(index)-1:
                temp = temp.siguiente
                contador +=1
            print("Dato eliminado: ", str(temp.siguiente.dato))
            temp.siguiente = temp.siguiente.siguiente

    def eliminarUltimo(self):
        if self.tamaño() == 1:
            self.cabeza = None
        elif self.tamaño() == 2:
            self.cabeza.siguiente = None
        elif self.tamaño() > 2:
            temp = self.cabeza
            while temp.siguiente.siguiente:
                temp = temp.siguiente
            temp.siguiente = None
        else:
            print("NO esisten elementos")
        

    def insertarDentro(self,index, dato):
        if index > self.tamaño():
            print("No se puede insertar, no existe esa posicion aun")
        elif index <= 0:
            print("No se puede insertar en la posicion indicada")
        elif index == 1:
            self.insertarInicio(dato)
        else:
            temp = self.cabeza
            contador = 1
            while contador != int(index)-1:
                temp = temp.siguiente
                contador +=1
            temp2 = temp.siguiente
            temp.siguiente = Nodo(dato)
            temp = temp.siguiente
            temp.siguiente = temp2





if __name__ == "__main__":
    lista = ListaSimple()
    lista.insertar("cosa1")
    lista.insertar("cosa2")
    lista.insertar("cosa3")
    lista.insertar("cosa4")
    lista.insertar("cosa5")
    lista.insertar("cosa6")
    lista.insertar("cosa7")
    lista.insertarInicio("cosa0")

    lista.mostrar()
    print("Datos: ",lista.tamaño())
    
    print(lista.buscar("cosa1"))

    lista.eliminar(3)
    lista.mostrar()
    print("Datos: ",lista.tamaño())

    lista.insertarDentro(2,"extra")
    lista.mostrar()
    lista.insertarDentro(5,"extra2")
    lista.mostrar()

    lista.eliminarUltimo()
    lista.mostrar()