def descuento(categoria):
    precio = float(input('Introduce el precio del producto:'))
    if categoria == "productos lacteos":
        return "Descuento de 10%. Por pagar:"+ str(precio - precio*0.1)
    elif categoria == "productos horneados":
        return "Descuento de 30%. Por pagar:"+ str(precio - precio*0.3)
    else:
        return "Por pagar:"+ str(precio)

categoria = ''
while (categoria != "cancelar"):
    categoria = input("Introduce la categoría:")
    if categoria != "cancelar":
        print(descuento(categoria))
    else:
        print("Compra cerrada")