/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Analizadores;
import java.util.LinkedList;
/**
 *
 * @author Pc
 */
public class CalculadoraDePila {
    /*push 4 push 5 add push 4 mult  push 72 div  print*/ 
    private LinkedList<Integer> pila = new LinkedList<Integer>();
    
    public void add(){
        pila.push( pila.pop() +pila.pop());
    }

    public void sub(){
        pila.push( pila.pop() - pila.pop());
    }

    public void mult(){
        pila.push( pila.pop() * pila.pop());
    }

    public void div(){
        pila.push( pila.pop() / pila.pop());
    }

    public void print(){
        System.out.println("hola"+ pila.pop());
    }

    public void push(Integer pNumber){
        pila.push(pNumber);
    }
}

