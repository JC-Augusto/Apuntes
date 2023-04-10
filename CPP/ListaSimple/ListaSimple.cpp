#include "ListaSimple.h"
#include <iostream>

void ListaSimple::agregarLista(int parametro){
    Nodo* temporal = new Nodo();
    temporal->dato = parametro;
    temporal->siguiente = cabeza;
    cabeza = temporal;
}

void ListaSimple::mostrarLista(){
    Nodo* temporalrecorrido = cabeza;
    cout<<"Imprimiendo la lista simple"<<endl;
    while(temporalrecorrido != NULL){
        cout<<temporalrecorrido->dato<<endl;
        temporalrecorrido = temporalrecorrido->siguiente;
    }
};