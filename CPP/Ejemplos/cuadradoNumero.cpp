/*

Escriba una funcion llamada al_cuadrado() que calcule el cuadrado del valor que se le trasmite y se despliegue
el resultado. La funcion debera ser capaz de  evaluar al cuadrado numeros flotantes.

*/

#include <iostream>

using namespace std;

//prototipo de función
void al_cuadrado(float numero);

int main (){
    float numero;
    cout << "Ingrese un numero: ";
    cin >> numero;

    al_cuadrado(numero);
};

void al_cuadrado(float numero){
    float resultado;
    resultado = numero * numero;
    cout << "\nEl cuadrado del numero es: "<< resultado <<endl;
}