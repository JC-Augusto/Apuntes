class Square():
    
    def area(self,x):
        return x*x

figure = Square()
side_length = int(input("Ingresa la longitud del lado del cuadrado: "))
print(figure.area(side_length))