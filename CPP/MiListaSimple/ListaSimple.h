#include "Nodo.h"

using namespace std;

class ListaSimple{
    public:
    Nodo* cabeza;
    
    ListaSimple(){
        cabeza = NULL;
    }

    void agregarLista(string valor);
    void eliminarLista();
    void mostrarLista();
    void insertarInicio(string valor);
};