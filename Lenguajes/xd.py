def make_list(number):
    names = []
    for item in range(number):
        names.append(input("ingrese nombre con mayuscula:"))
    print(names)
    return names
number = int(input("cuantos nombres: "))
names = make_list(number)
for name in names:
    if name[0] == "A":
        print("Name:", name, " starts with A")