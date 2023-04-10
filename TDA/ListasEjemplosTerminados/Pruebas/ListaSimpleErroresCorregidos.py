class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
    
class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def insert(self,dato):
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

    def mostrar(self):
        temp = self.cabeza
        while temp:
            print(temp.dato, end="-->")
            temp = temp.siguiente
        print("Null")

    def tamaño(self):
        temp = self.cabeza
        contador = 0
        while temp:
            temp = temp.siguiente
            contador +=1
        return contador
    
    def buscar(self,dato):
        if self.cabeza == None:
            print("No existen datos")
        else:
            temp = self.cabeza
            while temp:
                if temp.dato == dato:
                    return True
                temp = temp.siguiente
            return False
    
    def posicion(self,dato):
        contador = 1
        temp = self.cabeza
        while temp.dato != dato:
            if temp.siguiente != None:
                temp = temp.siguiente
                contador +=1
            else:
                return "No encontrado"
        return contador
    
    def eliminarUltimo(self):
        temp = self.cabeza
        if temp != None:
            if self.tamaño() == 1:
                temp = None
            elif self.tamaño() == 2:
                temp.siguiente = None
            elif self.tamaño() > 2:
                while temp.siguiente.siguiente != None:
                    temp = temp.siguiente
                temp.siguiente = None
        else:
            return "Lista vacia"

    def eliminar(self,index):
        temp = self.cabeza
        contador = 1
        if index > self.tamaño():
            print("El valor buscado excede el tamaño de la lista")
        elif index == self.tamaño():
            self.eliminarUltimo()
        elif index == 1:
            self.cabeza = temp.siguiente
        elif index > 1:
            for i in range(int(index)-2):
                temp = temp.siguiente
            temp.siguiente = temp.siguiente.siguiente
        elif index < 1:
            print("Ingrese un valor valido")

    def insertarDentro(self,index,dato):
        if index < 1:
            print("0 o negativos no validos")
        elif index > self.tamaño()+1:
            print("Opcion no valida ")
        elif index == self.tamaño()+1:
            self.insert(dato)
        elif index == 1:
            self.insertarInicio(dato)
        elif index > 1:
            temp = self.cabeza
            contador = 2
            while int(index) != contador:
                temp = temp.siguiente
                contador +=1
            temp2 = temp.siguiente
            temp.siguiente = Nodo(dato)
            temp = temp.siguiente
            temp.siguiente = temp2



if __name__ == "__main__":
    lista = ListaSimple()
    lista.insert("dato1")
    lista.insert("dato2")
    lista.insert("dato3")
    lista.insert("dato4")
    
    lista.insert("dato5")
    lista.insert("dato6")
    lista.mostrar()


    lista.insertarDentro(8,"extra1")
    lista.mostrar()
