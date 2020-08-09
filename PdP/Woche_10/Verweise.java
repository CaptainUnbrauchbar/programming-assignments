/**
 * Verweise.java
 *  
 * Ein Programm, das die Funktionsweise von Verweisen demonstriert.
 */

class Verweise {

  public static void main(String[] args) {

	// Definitionen
	Point p1, p2;

	// Initialisieren

	p1 = null;
	p2 = new Point();

	System.out.println();
	System.out.println("Die Werte der Referenzvariablen sind:");
	System.out.println();
	System.out.println("   p1 = " + p1);
	System.out.println("   p2 = " + p2);
	System.out.println();

	// Das kann zur Zeit nicht gut gehen:
	// System.out.println("   p1 = (" + p1.x + "," + p1.y + ")");

	// Erzeugen von p1 und Verschieben von p2

	p1 = new Point();
	p2.moveTo(2,3);

	System.out.println();
	System.out.println("Klassen sind Referenz-Datentypen:");
	System.out.println();
	System.out.println("   p1 = " + p1);
	System.out.println("   p2 = " + p2);
	System.out.println();

	System.out.println("   p1 = (" + p1.x + "," + p1.y + ")");
	System.out.println("   p2 = (" + p2.x + "," + p2.y + ")");
	System.out.println();

	System.out.println("Jetzt wird p2 = null gesetzt.");
	System.out.println();

	p2 = p1;

	System.out.println("   p1 = " + p1);
	System.out.println("   p2 = " + p2);
	System.out.println();

	System.out.println("Nach dem Verschieben von p1 nach (4,5):");

	p1.moveTo(4,5);

	System.out.println();
	System.out.println("   p1 = (" + p1.x + "," + p1.y + ")");
	System.out.println("   p2 = (" + p2.x + "," + p2.y + ")");
	System.out.println();
  }
} 

// Verweise

