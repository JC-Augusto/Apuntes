#include <iostream>
#include <conio.h>

using namespace std;

/*
========= PUNTEROS =========

&n = la dirección de n
*n = la variable cuya dirección esta almacenada en n 

*/

int main(){

    int num;

    num = 20;

    cout << "Numero: "<< num << endl;
    cout << "Direccion de num: "<< &num << endl;

    getch();
    return 0;
}