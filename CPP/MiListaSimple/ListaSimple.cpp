#include <iostream>
#include "ListaSimple.h"

void ListaSimple::agregarLista(string dato){
    Nodo* temp;
    if(cabeza == NULL){
        cabeza  = new Nodo(dato);
    }
    else{
        temp = cabeza;
        while (temp->siguiente != NULL){
            temp = temp->siguiente;
        }
        temp->siguiente = new Nodo(dato);
    }
}

void ListaSimple::mostrarLista(){
    Nodo* temp = cabeza;
    while(temp != NULL){
        cout << temp->valor <<endl;
        temp = temp->siguiente;
    }
    cout << "fin...";
}

void ListaSimple::insertarInicio(string dato){
    Nodo* temp;
    if(cabeza == NULL){
        cabeza = new Nodo(dato);
    }
    else{
        temp = cabeza;
        cabeza = new Nodo(dato);
        cabeza->siguiente = temp;
    }
}