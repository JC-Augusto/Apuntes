/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Utils;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

/**
 *
 * @author jca19
 */
public class Analizador {
    public Analizador() {
        
    }
    public void interpretar(String ruta) throws FileNotFoundException{
        analizadores.Sintactico pars;
        
        try{
            pars = new analizadores.Sintactico(new analizadores.Lexico(new FileInputStream(ruta)));
            pars.parse();
            
        }catch (Exception ex){
            System.out.println("Error en la compilacion ");
        }
    }
}
