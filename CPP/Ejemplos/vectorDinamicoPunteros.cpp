#include <iostream>
#include <conio.h>
#include <stdlib.h>

using namespace std;

//prototipos de funcion
void pedirNotas();

int main (){

    pedirNotas();

    getch();
    return 0;
}

void pedirNotas(){
    int notas, *calif;

    cout << "Ingrese la cantidad de notas: " ;
    cin >> notas;

    calif = new int[notas];

    for(int i=0; i<notas; i++){
        cout << "\nIngrese la nota: "; 
        cin >> calif[i];
    }

    cout << "Las notas son: " << endl;

    for(int i=0; i<notas; i++){
        cout << calif[i] <<endl;
    }

    delete[] calif;// liberando el espacio usado en el arreglo dinamico 

}