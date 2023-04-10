#include <stddef.h>


class Nodo{
    //atributos y metodos
    public: 
        int dato;
        Nodo* siguiente;

        //constructor
        Nodo(){
            siguiente = NULL;
            dato = 0;
        }
    private:
};