class Appli
{
	public static void main(String[] Args)
	{
		Square s = new Square();
		s.setSize(2);
		System.out.println(s.getSize());
		
		Circle c = new Circle();
		c.setSize(1);
		System.out.println(c.getArea());
	}
}
