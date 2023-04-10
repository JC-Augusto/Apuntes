/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package ejemplo1;

import java.io.StringReader;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Pc
 */
public class Ejemplo1 {

    public static void main(String[] args) {
         String prueba ="push 4 push 5 add  print  ";
        try {
        Analizadores.parser parse;
        parse = new Analizadores.parser( new Analizadores.Lexico(new StringReader( prueba)));
        
            parse.parse();
        } catch (Exception ex) {
            Logger.getLogger(Ejemplo1.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}