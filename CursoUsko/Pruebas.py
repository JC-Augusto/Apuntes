def generarMultipolosDe7(limite):
    numero = 1
    listaNumeros = []

    while numero <= limite:
        listaNumeros.append(numero*7)
        numero +=1
    return listaNumeros


def generadorMultiplosDe7(limite):
    numero = 1
    while numero <= limite:
        yield numero * 7 
        numero +=1

obtenerMultiplosDe7 = generadorMultiplosDe7(5)

for n in obtenerMultiplosDe7:
    print(n)

print(next(obtenerMultiplosDe7))
print("aca hay 1000 lineas de codigo")
print(next(obtenerMultiplosDe7))
print("aca hay muchas lineas de codigo")
print(next(obtenerMultiplosDe7))