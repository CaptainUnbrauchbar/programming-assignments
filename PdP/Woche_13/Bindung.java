/** Bindung.java
 * 
 * Eine Klasse, die am Beispiel des figure-Pakets
 * statische und dynamische Typen ausprobiert
 */

import figure.*;

class Bindung {

  public static void main(String[] args) {

	Figure f = new Square();
	f.moveTo(2,3);  
	f.area();
	f.show();

	if (f instanceof Square) {
	  ((Square)f).show();
	}

	System.out.println("Flaecheninhalt: " + f.area());
	f = new Circle(10);
	System.out.println("Flaecheninhalt: " + f.area());

  }
}

// Bindung
