from Lista import *
from xml.dom import minidom

ls = LSimples()
list = LSimples()

menu = 0
contador = 0
while menu != 5 :
    print("""MENU
    1. Agregar
    2. Listar
    3. Buscar
    4. ListaXML
    5. Salir""")
    menu = int(input("Ingrese ua opcion: "))

    if menu == 1:
        contador +=1
        dato = input("Ingrese el nombre: ")
        nod = Nodo(dato,contador)
        ls.agregarFin(nod)
    elif menu == 2:
        ls.listar()
    elif menu == 3:
        buscado = int(input("ingrese el indice buscado: "))
        result = ls.buscar(buscado)
        if result is not None:
            print(result)
        else: 
            print("Registro no enconrado")
    elif menu == 4: 
        ruta = ("Documentos/prueba.xml")
        xml = minidom.parse(ruta)
        
        dimensionX = xml.getElementsByTagName("x")[3]
        dimensionY = xml.getElementsByTagName("m")[1]
        print("imprimiendo posicion inicio: ")
        print(dimensionX.firstChild.data)
        print("fin posicioon inicio")
        print(dimensionY.firstChild.data)
        print(dimensionX)

