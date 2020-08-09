package figure;

public class Square extends Figure
{
	protected int length;
	
	Square()
	{
		super();
		length = 0;
	}
	
	Square(int lengthInit)
	{
		super();
		length = lengthInit;
	}
	
	Square(int xInit, int yInit)
	{
		super(xInit,yInit);
		length = 0;
	}
	
	Square(int xInit, int yInit, int lengthInit)
	{
		super(xInit,yInit);
		length = lengthInit;
	}
	
	void setSize(int size)
	{
		length = size;
	}
	int getSize()
	{
		return length;
	}
	double getArea()
	{
		return length*length;
	}
	double getPerm()
	{
		return length*4;
	}
}
