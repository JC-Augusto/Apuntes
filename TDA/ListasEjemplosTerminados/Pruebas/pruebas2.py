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

    def obtenerCaracter(self,dato1,dato2) -> int:
        x = 0
        limite1 = len(dato1)
        limite2 = len(dato2)
        if limite1 < limite2:
            limite = limite1
        else:
            limite = limite2
        while dato1[x] == dato2[x]:
            x += 1
            if limite == x:
                return x-1
        return x

    def ordenarPalabras(self):
        temp = self.cabeza
        for i in range(self.tamaño()-1):
            for j in range(self.tamaño()):
                if temp.siguiente:
                    a = str(temp.siguiente.dato)
                    b = str(temp.dato)
                    caracter = self.obtenerCaracter(a,b)
                    if ord(a[caracter]) < ord(b[caracter]):
                        aux = temp.dato
                        temp.dato = temp.siguiente.dato
                        temp.siguiente.dato = aux
                        temp = temp.siguiente
                    else:
                        temp = temp.siguiente
            temp = self.cabeza

if __name__ == "__main__":
    lista = ListaSimple()

    lista.insert("hola03")
    lista.insert("hola02")
    lista.insert("hola22")
    lista.insert("hola02")
    lista.insert("hola22")
    lista.mostrar()

    lista.ordenarPalabras()
    lista.mostrar()