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
    print(x)

for x in range(0,scanner.getTamañoListaDeListas()):
    scanner.generarDoubleMirrorVarios(x)
    print(x)

for x in range(0,scanner.getTamañoListaDeListas()):
    scanner.generarMirrorXVarios(x)
    print(x)

for x in range(0,scanner.getTamañoListaDeListas()):
    scanner.generarMirrorYVarios(x)
    print(x)

config = imgkit.config(wkhtmltoimage=f"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe")
imgkit.from_file("Proyecto1/templates/Pokeball.html",f"Proyecto1/Imagenes/{scanner.getName()}.png", config=config)
