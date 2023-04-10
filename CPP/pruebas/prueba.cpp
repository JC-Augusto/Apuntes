#include <iostream>
using namespace std;

int main(){
    cout << "Hola mundo";
    int a,b, suma = 0;
    cout << "Ingresa un numero: ";
    cin >> a;
    cout << "Ingresa otro numero: ";
    cin >> b;

    suma = a+b;

    cout << "La suma es: " << suma;

    return 0;
}

/*
CONDICIONALES

if (condición){
    instrucciones1;
}
else if(condicion) {
    instrucciones2;
}
else{
    instrucciones2
}

switch(expresión){
    case literal1:
        instrucciones1;
        break;
    case literal2:
        instrucciones2;
        break;
    default:
        instrucciones por defecto;
        break;
}

BUCLES 

while(expresicon logica){
    conjunto de instrucciones;

}

do{
    conjunto de instrucciones;
}while(expresón lógica);


for (expresion1; expresión lógica; expresion2){
    conjunto de instrucciones;
}

expresion1 = inicio de las iteraciones
expresion l. = hasta cuando se ejecuta el iterador
expresion2 = con que frecuencia cambia el iterador


*/