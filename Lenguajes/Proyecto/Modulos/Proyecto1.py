from Metodos import *



if __name__ == '__main__':
    ruta = cargarArchivo()
    archivo= leerArchivo(ruta)
    print(archivo)

    hola = "hola como estan"

    if hola.isalpha():
        print("helo")
    else: 
        print("No hello ")