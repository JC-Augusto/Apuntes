#include "Nodo.h"

using namespace std;

class ListaSimple{
    //metodos y atributos

    public:
    //atributos
        Nodo* cabeza = NULL;
    //inicializamos su constructor
        ListaSimple(){
            cabeza = NULL;
        }

    //metodos que se utilizaran 
    void agregarLista(int valor);
    void mostrarLista();
    private:
};