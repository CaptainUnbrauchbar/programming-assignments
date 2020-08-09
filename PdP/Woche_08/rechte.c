/* rechte.c
 *
 * simuliert die Rechteberechnung bei gesetzter umask in UNIX:
 * bitweise UND-Verknuepfung von Grundwert und negierter umask
 */

#include <stdio.h>

int main() {
	unsigned int grundwert, umask, rechte;
	char type;

	// Grundwert einstellen
	grundwert = 0666;	// Oktalzahl

	printf("Wollen Sie Rechte fuer ein Verzeichnis einstellen (j/n)? ");
	scanf("%c", &type);

	if (type == 'j'){
		grundwert = 0777;
	}

	printf("Geben Sie den Wert fuer umask ein: ");
	scanf("%o", &umask);

	// Rechte berechnen


	printf("Ihre Rechte: %o\n", rechte);
	
	return 0;
}
