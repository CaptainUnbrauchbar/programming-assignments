#include <stdio.h>

int main()
{
	char *statS = "Hallo PdP!";
	char dynS[] = "Hallo PdP!";
	
	//statS[1] = 'e';
	dynS[1] = 'e';
	
	int i;
	char *h = "neuer String";
	for(i=0;i<10;i++)
	{
		dynS[i] = h[i];
	}
	printf("%s %s\n", statS, dynS);
	return 0;
}
