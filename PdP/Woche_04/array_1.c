/* array_1.c
 * 
 * Adressierung von Array-Elementen
 * Indizes vs. Pointer
 */

#include <stdio.h>

int main() {

	int i;
	int ar [4];
	ar[0] = 10;
	ar[1] = 20;
	ar[2] = 30;
	ar[3] = 40;
	
	printf("\nar: %p\t &ar[0]: %p", ar, &ar[0]);
	printf("\n\nElemente von ar, indiziert:\n");
	
	for ( ; ; i++){			// hier ergaenzen!!!
		printf("%d\t", ); 	// hier ergaenzen!!!
	}

	printf("\n\nAdressen:\n");
	for ( ; ; i++){			// hier ergaenzen!!!
		printf("%p\t", ); 	// hier ergaenzen!!!
	}
	
	printf("\n\nElemente von ar, referenziert:\n");
	for ( ; ; i++){ 		// hier ergaenzen!!!	
		printf("%d\t", );	// hier ergaenzen!!! 
	}
	
	printf("\n\nAdressen:\n");
	for ( ; ; i++){			// hier ergaenzen!!!
		printf("%p\t", );	// hier ergaenzen!!! 
	}
	
	printf("\n\n");
	return 0;
}
