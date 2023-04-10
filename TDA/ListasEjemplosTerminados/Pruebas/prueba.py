"""total = 150
x = int((total ** (1/2))*2)
cantidadx = 1


if x%2 == 0:
    mitad = int(x/2)
else:
    mitad = int((x-1)/2)

cantidad = mitad

print("la mitad es: ", mitad)

for i in range(x):

    for j in range(cantidad):
        print(" ", end= " ")

    for rombo in range(cantidadx):
        print("x",end=" ")

    if i < mitad:
        cantidad -=1
        cantidadx += 2
    else:
        cantidad +=1
        cantidadx -= 2


    print("")"""


