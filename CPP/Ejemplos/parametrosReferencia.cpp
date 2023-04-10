// Paso de parametros por referencia

#include <iostream>
#include <conio.h>

using namespace std;

//propotipo usando paso por referencia
void valNuevo(int&,int&);

int main(){
    int numero1,numero2;
    cout<< "Digite dos numeros: ";
    cin>> numero1 >> numero2; 

    valNuevo(numero1,numero2);

    cout << "El nuevo valor del primer numero es: " << numero1 <<endl;
    cout << "El nuevo valor del segundo numero es: "<< numero2 <<endl;

    getch();
    return 0;
};

void valNuevo(int& xnum, int& ynum){
    cout<<"El valor del primer numero es: "<<xnum <<endl;
    cout<<"El valor del segundo numero es: "<<ynum <<endl;

    xnum = 100;
    ynum = 200;
}