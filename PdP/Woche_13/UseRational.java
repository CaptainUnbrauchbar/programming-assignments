// UseRational.java.1-3 (Version .1-3)

import java.util.Scanner;

class UseRational {

  public static void main(String[] args) {

    // Definitionen
    Scanner scanner = new Scanner(System.in);

    Rational r;
    

    // Dialog
    System.out.println();
    System.out.println();
    System.out.print("Geben Sie den Zaehler ein: ");
    int a = scanner.nextInt();
    System.out.print("Geben Sie den Nenner ein: ");
    int b = scanner.nextInt();
    System.out.println();

    // Rational-Objekt erzeugen
    r = new Rational(a,b);
        
    
    // Methodenaufrufe
    System.out.println(r.toString());   	  // Bruch ausgeben
    System.out.println(r.toStringReduced());  // Bruch gekuerzt ausgeben

    System.out.println(r.toString());
    System.out.println();
  }
}

// UseRational

