/*

Ejercicio 1: Escriba una funcion llamada mult() que acepte dos números en punto 
flotante como parámetros, multiplique estos dos números y despliegue el resultado

*/

#include <iostream>
#include <conio.h>

using namespace std;

//variables globales
float x,y;

//función prototipo

void pedirDatos();
void mult(float x, float y);

int main (){

    pedirDatos();
    mult(x,y);

    getch();
    return 0;
}

void pedirDatos(){
    cout << "Ingrese un numero; "; cin >> x;
    cout << "\nIngrese otro numero: "; cin >> y;
}

void mult(float x, float y){
    float resultado;
    resultado = x * y;
    cout << "\nEl reslutado es: " <<resultado;
}