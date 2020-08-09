/** StreamDema.java
 *
 *  Eine Applikation, die das Verhalten einfacher
 *  Eingabestroeme in Java demonstriert
 */

import java.io.*;

public class StreamDemo {
 
  public static void main(String[] args) throws Exception {


    System.out.print("Bitte geben Sie Zeichen ein: ");

    System.in.read(); 		// Verbrauchen des ersten Zeichens

    int tmp = System.in.read(); // Verbrauchen und Speichern des 2. Zeichens
    System.out.println(tmp + " : " + (char)tmp); 	


    InputStreamReader ein = new InputStreamReader(System.in);

    tmp =   ein.read();		// Verbrauchen und Speichern des 3. Zeichens
    System.out.println(tmp + " : " + (char)tmp);	


    BufferedReader inp = new BufferedReader(ein);

    String tmpStr = inp.readLine(); // Lesen und Speichern der restlichen
                                    // Zeichen bis zum Zeilenende
    System.out.println(tmpStr);
    
    System.out.println(ein.getEncoding());

  }
}

// StreamDemo

