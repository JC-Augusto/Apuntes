from Modulos.Analizador import Analizador
from Modulos.FuncionesAuxiliares import *
import imgkit

DatosArchivo = leerArchivo(rutaArchivo())

scanner = Analizador()
scanner.analizar(DatosArchivo)

#scanner.imprimirErrores()
#scanner.imprimirTokens()
#scanner.imprimirDatosImagen()
#scanner.imprimirListaColores()

scanner.generarTablaErrores()
scanner.generarTablaTokens()
"""
scanner.generarImagenOriginal()
scanner.generarImagenMirrorX()
scanner.generarImagenMirrorY()
scanner.generarImagenDoubleMirror()

print(f"Imagenes en archivo: {scanner.getTamañoListaDeListas()}")
print(f"El nombre es: {scanner.getName()}")

print(f"el color es: {scanner.getNewColor()}")
print(f"filtros: {scanner.getFiltros()}")
"""

for x in range(0,scanner.getTamañoListaDeListas()):
    scanner.generarImagenOriginalVarios(x)
    

for x in range(0,scanner.getTamañoListaDeListas()):
    scanner.generarDoubleMirrorVarios(x)
    

for x in range(0,scanner.getTamañoListaDeListas()):
    scanner.generarMirrorXVarios(x)
    

for x in range(0,scanner.getTamañoListaDeListas()):
    scanner.generarMirrorYVarios(x)
    



config = imgkit.config(wkhtmltoimage=f"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe")
for x in range(0,scanner.getTamañoListaDeListas()):
    imgkit.from_file(f"Proyecto1/templates/{scanner.getName(x)}.html",f"Proyecto1/Imagenes/{scanner.getName(x)}.png", config=config)
    imgkit.from_file(f"Proyecto1/templates/{scanner.getName(x)}_MirrorX.html",f"Proyecto1/Imagenes/{scanner.getName(x)}_MirrorX.png", config=config)
    imgkit.from_file(f"Proyecto1/templates/{scanner.getName(x)}_MirrorY.html",f"Proyecto1/Imagenes/{scanner.getName(x)}_MirrorY.png", config=config)
    imgkit.from_file(f"Proyecto1/templates/{scanner.getName(x)}_DoubleMirror.html",f"Proyecto1/Imagenes/{scanner.getName(x)}_DoubleMirror.png", config=config)
