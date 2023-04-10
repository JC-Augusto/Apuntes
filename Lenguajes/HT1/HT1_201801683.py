class AL:

    def __init__(self):
        self.estado = 0
        self.indexCadena = 0
        self.aceptacion = True

    def analizar(self,cadena):
        self.estado = 0
        self.indexCadena = 0
        
        while self.indexCadena < len(cadena):
            if self.estado == 0:
                self.estado0(cadena[self.indexCadena])
            elif self.estado == 1:
                self.estado1(cadena[self.indexCadena])
            elif self.estado == 2:
                self.estado2(cadena[self.indexCadena])
            elif self.estado == 3:
                self.estado3(cadena[self.indexCadena])
            if self.aceptacion == False: 
                print("==================================================")
                print("           CADENA NO ACEPTADA")
                print("==================================================\n\n\n")
                break
            self.indexCadena +=1

    def indicadores(caracter, nodo, nodosiguiente):
        print("tengo: "+caracter+"eston en"+str(nodo)+" voy al "+str(nodosiguiente))


    def estado0(self,caracter):
        if caracter == "0":
            self.estado = 1
            print("tengo:" +caracter + " estoy en el estado 0 -> voy al 1")
        else:
            self.aceptacion = False 
            
    def estado1(self, caracter): 
        if caracter == "0":
            self.estado =2
            print("tengo:"+ caracter+ " estoy en el estado 1 -> voy al 2")
        elif caracter == "1":
            self.estado =3
            print("tengo:"+ caracter+" estoy en el estado 1 -> voy al 3")
        else: 
            self.aceptacion = False

    def estado2(self, caracter):
        if caracter in ["0","1"]:
            self.estado =1
            print("tengo:"+ caracter + " estoy en el estado 2 -> voy al 1")
        else:
            self.aceptacion = False

    def estado3(self, caracter):
        if caracter in ["0","1"]:
            self.estado =1
            print("tengo:"+caracter+ " estoy en el estado 3 -> voy al 1")
        elif caracter == "#":
            print("Encontre la almoadilla")
            print("==================================================")
            print("           CADENA ACEPTADA")
            print("==================================================\n\n\n")
        else:
            self.aceptacion = False

entrada = True
while entrada == True:
    print("\n\npara salir ingrese: salir, exit, s")
    print("==================================================")
    print("<<<<<<     AUTOMATA: 0(00|01|10|11)*1     >>>>>>>")
    print("==================================================")

    entrada = input("\nIngrese su cadena: ") + "#"
    if entrada == "salir#" or entrada == "exit#" or entrada == "s#":
        entrada = False
    else:
        scanner = AL()
        scanner.analizar(entrada)
        entrada = True
