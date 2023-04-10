/*

Punteros - Declaración de punteros

&n = La dirección de n
*n = la variable cuya dirección esta almacenada en n

*/

#include <iostream>
#include <conio.h>

using namespace std;

int main(){

    int numero = 20;

    cout << "El numero es: " << numero<< endl;
    cout << "La direccion de memoria del numero es: "<< &numero << endl;

    getchar();
    return 0;
}