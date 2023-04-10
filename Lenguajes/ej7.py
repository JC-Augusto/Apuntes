#Escribe la función perimeter() para calcular el perímetro
def perimeter(a,b):
    return (2*a)+(2*b)

#Escribe la función area() para calcular el área
def area(a,b):
    return a*b

a = int(input("Ingresa el primer lado del rectángulo: "))
b = int(input("Ingresa el segundo lado del rectángulo: "))

print('Perímetro =', perimeter(a,b))
print('Área =', area(a,b))