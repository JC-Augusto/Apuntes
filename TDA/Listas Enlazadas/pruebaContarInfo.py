import xml.etree.ElementTree as ET

myTree = ET.parse("Documentos/prueba.xml")
myRoot = myTree.getroot() #obtengo los datos del archivo XML

contadorDatos = 0
for x in myRoot[0]:
    if x.text == "\n\t\t\t": 
        pass
    else:
        """Genera el valor de las pociciones en el primer terreno por el [0]"""
        print(x.text)
        contadorDatos +=1

print(f"datos toatales = {contadorDatos}")
