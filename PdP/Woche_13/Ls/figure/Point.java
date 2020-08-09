/**
 * Datei: Point.java 
 *
 * Eine Klasse der Punkte einer Ebene 
 *
 */
package figure;

public class Point {

	// Instanzvariablen (Datenelemente)
	private int x, y;

	// Konstruktoren
	Point() {
		x = 0;
		y = 0;
	}

	Point(int xInit, int yInit) {
		x = xInit;
		y = yInit;
	}

	// Methoden zum Abfragen der Werte der Datenelemente
	int getX() {
		return x;
	}

	int getY() {
		return y;
	}

	void moveTo(int xNew, int yNew) {
		x = xNew;
		y = yNew;
	}
	
	void move(int xAdd, int yAdd)	{
		x+= xAdd;
		y+= yAdd;
	}

}

// Point
