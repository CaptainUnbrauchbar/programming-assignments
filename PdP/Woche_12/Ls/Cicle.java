import java.math.*;

class Circle extends Figure
{
	protected int radius;
	
	Circle()
	{
		super();
		radius = 0;
	}
	
	Circle(int radiusInit)
	{
		super();
		radius = radiusInit;
	}
	
	Circle(int xInit, int yInit)
	{
		super(xInit,yInit);
		radius = 0;
	}
	
	Circle(int xInit, int yInit, int radiusInit)
	{
		super(xInit,yInit);
		radius = radiusInit;
	}
	
	void setSize(int size)
	{
		radius = size;
	}
	int getSize()
	{
		return radius;
	}
	double getArea()
	{
		return Math.PI*radius*radius;
	}
	double getPerm()
	{
		return 2*Math.PI*radius;
	}
}
