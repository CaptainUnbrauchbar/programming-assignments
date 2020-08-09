class Gcd
{
	public static int gcd(int x, int y)
	{
		if (x == 0){ return y;}
		if (y == 0){ return x;}
		if (x < 0){ x = -x;}
		if (y < 0){ y = -y;}
		while (x != y) {
		  if (x > y){ x = x - y;}
		  else{ y = y - x;}
		}
		return x;
	}
}
