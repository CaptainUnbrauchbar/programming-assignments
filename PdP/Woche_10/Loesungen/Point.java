/**
 * Datei: Point.java 
 *
 * Eine Klasse der Punkte einer Ebene 
 *
 */

class Point {

  // Instanzvariablen (Datenelemente)
  int x, y;

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

}

// Point
