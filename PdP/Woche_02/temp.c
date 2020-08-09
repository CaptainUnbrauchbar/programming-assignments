#include <stdio.h>
int main()
{
	printf("Fahrenheit\tCelsius\n");
	int i;
	int x;
	for(i = 0;i<=300;i=i+20)
	{
		x = 5 * (i-32)/9;
		printf("%d\t\t%d\n",i,(int) x);
	}
	return 0;
}
