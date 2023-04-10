#include <stddef.h>
#include <string>

using namespace std;

class Nodo{
    public:
    string valor;
    Nodo* siguiente;

    Nodo(){
        siguiente = NULL;
        valor = "";
    }

    Nodo(string dato){
        siguiente = NULL;
        valor = dato;
    }
};