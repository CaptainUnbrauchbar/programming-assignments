/**
 * UsePoint.java 
 * 
 * Ein Programm, das Objekte der Klasse Point erzeugt und manipuliert.
 */

class UsePoint {

  public static void main(String[] args) {

	// Erzeugen von zwei Exemplaren des Typs Point mit den Namen p und q;
	// p soll an den Koordinaten (30,10) erzeugt werden,
	// q mit dem parameterlosen Konstruktor am Koordinatenursprung.

	Point p = new Point(30,10);	   
	Point q = new Point();

	// Verschieben von q auf die Koordinaten (40,40) 

	q.moveTo(40,20);	

	// Ausgabe der Attribute von p und q
	System.out.println();
	System.out.println("   x-Koordinate von p: " + p.getX());
	System.out.println("   y-Koordinate von p: " + p.getY());
	System.out.println();
	System.out.println("   x-Koordinate von q: " + q.getX());
	System.out.println("   y-Koordinate von q: " + q.getY());
	System.out.println();
  }
}

// UsePoint
