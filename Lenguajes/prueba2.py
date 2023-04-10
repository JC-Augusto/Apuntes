


categoria = ''


while (categoria != "cancelar"):
    categoria = input("Introduce la categoría:")
    if categoria != "cancelar":
        precio = float(input('Introduce el precio del producto'))
        if categoria == "productos lacteos":
            print("Descuento de 10%. Por pagar:", precio - precio*0.1)
        elif categoria == "productos horneados":
            print("Descuento de 30%. Por pagar:", precio - precio*0.3)
        else:
            print("Por pagar:", precio)
    else:
        print("cerrando programa")