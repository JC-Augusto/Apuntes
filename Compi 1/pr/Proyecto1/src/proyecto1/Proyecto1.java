/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package proyecto1;

import UI.Principal;
import UI.Principal;
import Utils.Analizador;
import java.io.FileNotFoundException;

/**
 *
 * @author jca19
 */
public class Proyecto1 {
    public static void main(String[] args) throws FileNotFoundException {
        Analizador a = new Analizador();
        a.interpretar("./public/entrada.txt");
        //Principal v = new Principal();
        //v.setVisible(true);
        //System.out.println("Tambien aqui");
    } 
}
