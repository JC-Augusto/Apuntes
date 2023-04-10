/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejemplojlex;

import Utils.Analizador;

/**
 *
 * @author jca19
 */
public class EjemploJLex {

    
    public static void main(String[] args) {
        Analizador a = new Analizador();
        a.interpretar("./public/entrada.txt");
        
    }
    
}
