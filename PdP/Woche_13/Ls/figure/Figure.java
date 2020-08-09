package figure;

public abstract class Figure
{
	protected Point pos;
	
	Figure()
	{
		pos = new Point();
	}
	
	Figure(int xInit, int yInit)
	{
		pos = new Point(xInit, yInit);
	}
	
	void moveTo(int xNew, int yNew)
	{
		pos.moveTo(xNew, yNew);
	}
	
	void move(int xAdd, int yAdd)
	{
		pos.move(xAdd, yAdd);
	}
	
	abstract void setSize(int size);
	abstract int getSize();
	abstract double getArea();
	abstract double getPerm();
}
