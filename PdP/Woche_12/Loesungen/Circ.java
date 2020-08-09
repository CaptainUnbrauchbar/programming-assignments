public class Circ extends Square{
	
	private int r;

	public Circ(){
			super();
			r=1;
	}
	
	public Circ(int r){
			super(r);
		}
	
	public Circ(int x, int y, int r){
		super(x,y,r);
		}
	
	// Groesse abfragen
	public int getSize() {
		return r;
	}

	// Groesse aendern
	public void resize(int r) {
		this.r = r;
	}

	// Flaecheninhalt
	public double area() {
		return Math.PI * r * r;
	}

	// Umfang
	public double perimeter() {
		return 2 * Math.PI * r;
	}



}
