/* plantillas de función 

Ejemplo: sacar el valor absoluto de un numero

problema... Que tipo de numero? negativo, entero, flotante...? 

para eso se utilizan los prototipos de función 
*/

#include <iostream>
#include <conio.h>

using namespace std;

// Prototipo de función 

template <class TipoD>
void mostrarAbs(TipoD numero);

int main(){
    int n1 = 56;
    int n2 = -10;
    float n3 = 11.45;
    double n4 = 44.23;

    mostrarAbs(n1);
    mostrarAbs(n2);
    mostrarAbs(n3);
    mostrarAbs(n4);

    getch();
    return 0;
};


//Esto nos ayudara a que se pueda ingresar cualquier tipo de dato "Gracias a la plantilla creada"
template <class TipoD>
void mostrarAbs(TipoD numero){
    if(numero < 0){
        numero = numero *- 1;
    }
    cout << "El valor absoluto del numero es: "<< numero<<endl;
};