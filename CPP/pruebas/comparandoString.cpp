#include <iostream>
#include <string>

using namespace std;

int main(){

    string nombre = "gato";

    string nombreC;

    cout << "ingrese el nombre: "; cin >> nombreC;

    if (nombre == nombreC){
        cout << "Son iguales";
        
    }
    else{
        cout << "Son diferentes";
    }

    return 0;
}