from AnalizadorLexico import AnalizadorLexico

def leerArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

def escribirArchivo(ruta, contenido):
    archivo = open(ruta, 'w')
    archivo.write(contenido)
    archivo.close()

if __name__ == '__main__':
    #Leemos el archivo de entrada
    cadena = leerArchivo("entrada.txt")

    #Instanciamos un nuevo analizador lexico o scanner
    scanner = AnalizadorLexico()

    #Enviamos la cadena a analizar
    scanner.analizar(cadena)
    
    scanner.impTokens()
    scanner.impErrores()