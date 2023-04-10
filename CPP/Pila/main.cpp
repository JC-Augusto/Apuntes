#include <iostream>
#include "ListaSimple.cpp"

using namespace std;

int main(){
    ListaSimple lista;
    lista.agregarLista(5);
    lista.agregarLista(10);
    lista.agregarLista(15);
    lista.agregarLista(20);
    lista.agregarLista(25);
    lista.mostrarLista();
    return 0;
}