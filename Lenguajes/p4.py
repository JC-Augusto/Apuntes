def make_list(number):
    names = []
    for item in range(number): 
        names.append(input("ingrese su nombre con letra mayuscula"))
    print(names)

number = int(input("cuantos nombres ingresara?")) #numero de nombres
names = make_list(number)
for name in names:
    if name [0] == "A":
            print("Name", name, " starts with A")