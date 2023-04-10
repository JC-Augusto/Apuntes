//importaciones
#include <iostream>
#include "ListaSimple.cpp"

using namespace std;

int main(int argc, char** argv){
    ListaSimple lista;
    /*lista.agregarLista(5);
    lista.agregarLista(4);
    lista.agregarLista(3);
    lista.agregarLista(2);
    lista.agregarLista(1);
    lista.mostrarLista();
    */

    int cantidad;
    
    cout << "Cuantos elementos agregara? :";
    cin >> cantidad; 
    for (int i= 0; i < cantidad; i++){
        cout << "Ingrese su dato:";
        int dato;
        cin >> dato;l
        lista.agregarLista(dato);

    }
    lista.mostrarLista();
    return 0;
}