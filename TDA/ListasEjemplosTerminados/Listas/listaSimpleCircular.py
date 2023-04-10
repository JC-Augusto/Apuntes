
class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class ListaSimpleCircular:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self,dato):
        if self.cabeza == None:
            self.cabeza = Nodo(dato)
            self.cabeza.siguiente = self.cabeza
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = Nodo(dato)
            temp = temp.siguiente
            temp.siguiente = self.cabeza

    def tamaño(self):
        if self.cabeza == None:
            return 0
        else:
            temp = self.cabeza
            contador = 1
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
                contador += 1
            return contador
    
    def insertarInicio(self,dato):
        if self.cabeza == None:
            self.cabeza = Nodo(dato)
            self.cabeza.siguiente = self.cabeza
        else:
            tamaño = self.tamaño()
            temp = self.cabeza
            self.cabeza = Nodo(dato)
            self.cabeza.siguiente = temp
            for i in range(tamaño-1):
                temp = temp.siguiente
            temp.siguiente = self.cabeza
            

    def mostrar(self):
        if self.cabeza:
            temp = self.cabeza
            print(self.cabeza.dato,end="-->")
            while temp.siguiente != self.cabeza:
                print(temp.siguiente.dato, end="-->")
                temp = temp.siguiente
            print("Regrese a la cabeza")
        else:
            print("No hay datos")
    
    def buscar(self,dato):
        if self.cabeza == None:
            print("No existen datos")
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                if temp.dato == dato:
                    return True
                temp = temp.siguiente
            if temp.dato == dato:
                return True
            else:
                return False
    
    def posicion(self,dato):
        if self.cabeza == None:
            print("Lista vacia")
        else:
            contador = 1
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                if temp.dato == dato:
                    return contador
                contador += 1
                temp = temp.siguiente
            if temp.dato == dato:
                    return contador
            else:
                return "El dato buscado, no se encuentra en la lista"
    
    def eliminarUltimo(self):
        if self.cabeza == None:
            print("Lista vacia")
        elif self.tamaño() == 1:
            self.cabeza = None
        elif self.tamaño() == 2:
            self.cabeza.siguiente = self.cabeza
        elif self.tamaño() > 2:
            temp = self.cabeza
            while temp.siguiente.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = self.cabeza

    def eliminar(self,index):
        temp = self.cabeza
        tamaño = self.tamaño()
        if index <= tamaño and index >= 1:
            if index == 1 and temp.siguiente != self.cabeza:
                while temp.siguiente != self.cabeza:
                    temp = temp.siguiente
                self.cabeza = self.cabeza.siguiente
                temp.siguiente = self.cabeza
            elif index == 1 and temp.siguiente == self.cabeza:
                self.cabeza = None
                
            elif index == 2 and temp.siguiente.siguiente != self.cabeza:
                self.cabeza.siguiente = self.cabeza.siguiente.siguiente
            
            elif index == 2 and temp.siguiente.siguiente == self.cabeza:
                self.cabeza.siguiente = self.cabeza
            elif index > 2:
                if index == tamaño:
                    self.eliminarUltimo()
                else:
                    for i in range(index-2):
                        temp = temp.siguiente
                    temp.siguiente = temp.siguiente.siguiente
        else:
            print("valor no valido")

    def insertarDentro(self,index,dato):
        tamaño = self.tamaño()
        temp = self.cabeza
        if index > 0 and index < tamaño+2:
            if index == 1:
                self.insertarInicio(dato)
            elif index == tamaño+1:
                self.insertar(dato)

            elif index == 2:
                temp = temp.siguiente
                self.cabeza.siguiente = Nodo(dato)
                self.cabeza.siguiente.siguiente = temp
            elif index > 2:
                for i in range(index-2):
                    temp = temp.siguiente
                temp2 = temp.siguiente
                temp.siguiente = Nodo(dato)
                temp = temp.siguiente
                temp.siguiente = temp2
        else:
            print("No se puede agregar en esta posicion.")


if __name__ == "__main__":
    lista = ListaSimpleCircular()
    print("")


    lista.insertar("dato1")
    lista.insertar("dato2")
    lista.insertar("dato3")
    lista.insertar("dato4")
    lista.insertar("dato5")

    lista.mostrar()





