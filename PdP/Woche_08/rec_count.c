// rec_static.c

#include <stdio.h>

void decr(int n) {
	rec_out(--n);
	
}

void rec_out(int n) {
	int count = 1;
	printf("Die %d. Ausgabe.\n", count);
	count++;
	if (n > 1){
		decr(n);
	}
}

int main() {
	rec_out(6);
	return 0;
}
