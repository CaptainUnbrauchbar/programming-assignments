#include <stdio.h>
int main() 
{
	int a;
	for(a=12;a>=0;a=a-2)
	{
		if(a!=0)
		{
			printf("%d, ",a);
		}
		else
		{
			printf("%d\n",a);
		}
	}
	
	
	for(a=-1;a>=-13;a=a-2)
	{
		if(a!=-13)
		{
			printf("%d, ",a);
		}
		else
		{
			printf("%d\n",a);
		}
	}
	
	for(a=0;a<=9;a++)
	{
		if(a!=9)
		{
			printf("%d, ",a*a);		
		}
		else
		{
			printf("%d\n",a*a);
		}
	}
	
	return 0;
}
