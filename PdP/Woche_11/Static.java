/** Static.java
 *	
 *	Eine Klasse, die Effekte mit Klassenvariablen demonstriert.
 */

class Static {

	int n;
	static int snum;

	void increase() {
		n++;
		snum++;
	}

	void output() {
		System.out.println("n = " + n + ", snum = " +snum);
	}

	static void set(int n) {
		snum = n;
	}




	public static void main(String[] args) {

		Static ex1 = new Static();
		Static ex2 = new Static();

		ex1.output();
		ex2.output();
		System.out.println();

		ex1.increase();

		ex1.output();
		ex2.output();

		set(5);		// Aufruf statische Methode
		Static ex3 = new Static();

		System.out.println();
		ex1.output();
		ex2.output();
		ex3.output();
	}
}

// Static




