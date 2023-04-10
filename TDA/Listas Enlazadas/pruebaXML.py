import xml.etree.cElementTree as ET
from xml.dom import minidom


ruta = ("Documentos/prueba.xml")

xml = minidom.parse(ruta)  #Leyendo el archivo 

terrenos = xml.getElementsByTagName("terreno") #Devuelve los elementos (objetos)
print(len(terrenos)) #devuelve la cantidad de objetos que encuentra

for elementos in terrenos: 
    """Con esto sacamos los nombres de los atributos"""
    print(elementos.attributes['nombre'].value)

dimension = xml.getElementsByTagName("n")
print(dimension[1].firstChild.data)
