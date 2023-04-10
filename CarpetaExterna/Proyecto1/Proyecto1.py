from Modulos.Analizador import Analizador
from Modulos.FuncionesAuxiliares import *
import imgkit

menu =0
while menu != 5: 
    print("""Opciones:
    1. Carcar Archivo
    2. Generar reportes
    3. Generar html imagenes
    4. Generar imagenes
    5. Salir""")

    menu = int(input("Ingrese una opcion: "))
    if menu == 1:
        DatosArchivo = leerArchivo(rutaArchivo())
        scanner = Analizador()
        scanner.analizar(DatosArchivo)
    if menu == 2:
        scanner.generarTablaErrores()
        scanner.generarTablaTokens()
    if menu == 3:
        for x in range(0,scanner.getTamañoListaDeListas()):
            scanner.generarImagenOriginalVarios(x)
        for x in range(0,scanner.getTamañoListaDeListas()):
            scanner.generarDoubleMirrorVarios(x)
        for x in range(0,scanner.getTamañoListaDeListas()):
            scanner.generarMirrorXVarios(x)
        for x in range(0,scanner.getTamañoListaDeListas()):
            scanner.generarMirrorYVarios(x)
    if menu == 4:
        config = imgkit.config(wkhtmltoimage=f"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe")
        for x in range(0,scanner.getTamañoListaDeListas()):
            imgkit.from_file(f"Proyecto1/templates/{scanner.getName(x)}.html",f"Proyecto1/Imagenes/{scanner.getName(x)}.png", config=config)
            imgkit.from_file(f"Proyecto1/templates/{scanner.getName(x)}_MirrorX.html",f"Proyecto1/Imagenes/{scanner.getName(x)}_MirrorX.png", config=config)
            imgkit.from_file(f"Proyecto1/templates/{scanner.getName(x)}_MirrorY.html",f"Proyecto1/Imagenes/{scanner.getName(x)}_MirrorY.png", config=config)
            imgkit.from_file(f"Proyecto1/templates/{scanner.getName(x)}_DoubleMirror.html",f"Proyecto1/Imagenes/{scanner.getName(x)}_DoubleMirror.png", config=config)

#scanner.imprimirErrores()
#scanner.imprimirTokens()
#scanner.imprimirDatosImagen()
#scanner.imprimirListaColores()


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




3