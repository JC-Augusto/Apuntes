import xml.etree.ElementTree as ET
from ListaDatoxDato.Lista import *

myTree = ET.parse("Documentos/prueba.xml")
myRoot = myTree.getroot() #obtengo los datos del archivo XML
"""
print(myRoot.tag) # Imprime la primera etiqueta
print(myRoot[0].attrib) # imprime el atributo de la segunda etiqueta
print(myRoot[0].tag) # imrime el nombre de la segunda etiqueta

for x in myRoot[0]:
    print(x.tag, x.attrib)
"""

contadorDatos = 0
listaDatos = LSimples()
for x in myRoot[0]:
    #Genera el valor de las pociciones en el primer terreno por el [0]
    if x.text == "\n\t\t\t":
        pass
    else:   
        nodoDatos = Nodo(x.text,contadorDatos)
        contadorDatos +=1
        listaDatos.agregarFin(nodoDatos)

aux = listaDatos.cabeza
for x in range(0,5): 
    for y in range (0,3):   
        print(aux,end = "   ")
        aux = aux.sig
    print("\n")

