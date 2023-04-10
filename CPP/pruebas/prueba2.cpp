#include <iostream>
#include <conio.h>

using namespace std;

int main(){
    
    int vector[10];

    for(int i= 0; i<10; i++){
        vector[i] = i+1;
    }
    int total = 0;
    for(int i=0; i<10; i++){
        total += vector[i];
    }

    cout << "el total es:"<< total << endl;



    return 0;
}