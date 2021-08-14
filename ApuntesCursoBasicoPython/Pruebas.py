from array import array
from random import randint

def quicksort(arreglo,letras) -> list:
    """Debuelve las notas y nombres de forma ascendente """
    if len(letras) < 2:
        return arreglo
    
    menores, igual, mayores = [],[],[]
    menoresA, igualA, mayoresA = [],[],[]
    pivote = arreglo[randint(0,len(arreglo) - 1)]

    for elemento in arreglo:
        if elemento < pivote:
            menores.append(elemento)
            menoresA.append(elemento)
        elif elemento == pivote:
            igual.append(elemento)
            igualA.append(elemento)
        elif elemento > pivote:
            mayores.append(elemento)
            mayoresA.append(elemento)
    letras = menoresA
    return quicksort(menores)+igual+quicksort(mayores)

arreglo = [10,7,20,30,2]
l = ["a","b","c","d","e"]

print(quicksort(arreglo,l))