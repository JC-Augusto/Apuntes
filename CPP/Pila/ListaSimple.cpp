#include "ListaSimple.h"
#include <iostream>

void ListaSimple::agregarLista(int valor){
    Nodo* temporal = new Nodo();
    temporal->valor = valor;
    temporal->siguiente = cabeza;
    cabeza = temporal; 
}

void ListaSimple::mostrarLista(){
    Nodo* temporal = cabeza;
    while(temporal != NULL){
        cout << temporal->valor <<endl;
        temporal = temporal->siguiente;
    }
}

void ListaSimple::eliminarNodo(){
    
}
