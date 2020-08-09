#include <stdio.h>

// Makro
#define tab printf("\t");
// Main
int main()
{
	//Array (3 Zeilen, 4 Spalten) & Initialisierung
	int a[3][4] = {{0,1,2,3},{10,11,12}};
	int i; int j;
	// Ausgabe
	for(i = 0; i < (int) sizeof(a)/sizeof(typeof(a[0])); i++)
	{
		for(j = 0; j < (int) sizeof(a[i])/sizeof(int); j++)
		{
			printf("%d", a[i][j]); tab
		}
		printf("\n");
	}
	//Ende
	return 0;
}
