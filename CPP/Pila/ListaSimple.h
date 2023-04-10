#include "Nodo.h"

using namespace std;

class ListaSimple{
    //metodos y atributos

    public:
    //atributos
    Nodo* cabeza = NULL;

    //inicializamos el constructor
    ListaSimple(){
        cabeza = NULL;
    }

    //prototipos de funciones a usar en la lista simple
    void agregarLista(int valor);
    void mostrarLista();
    void eliminarNodo();
};
