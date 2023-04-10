#include <iostream>
#include "ListaSimple.cpp"

using namespace std;

int main(){
    ListaSimple lista;
    lista.agregarLista("hola");
    lista.agregarLista("Como estan");
    lista.agregarLista("El d1ia d3 hoy");
    lista.agregarLista("esto es");
    lista.agregarLista("una");
    lista.insertarInicio("prueba de strings");
    lista.mostrarLista();
    return 0;
}