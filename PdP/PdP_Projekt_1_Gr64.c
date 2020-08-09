
/*
 Praxis der Programmierung
 Projekt 1
 Abgabedatum: 2.6.2019

 Gruppennummer : <64>
 Gruppenmitglieder :
 - <Johnny Hänsel>			- MatrikelNr: 796033
 - <Florian Frankreiter>	- MatrikelNr: 796762
 - <Maximilian Metzner>		- MatrikelNr: 793692
*/

#include <stdlib.h>
#include <stdio.h>

struct le {
    int value;								// Initialisiert value (Wert von einem Listenelement)
    struct le * next;						// Definiert Adresszuweisung auf nächstes Element
};
typedef struct le listenelement;			// Ersetzt le durch bezeichnung Listenelement
typedef listenelement * list;				// setzt pointer

//funktion zum Einfügen eines Elements in die Liste an erste stellle
void insert(int v, list * l){
    listenelement * new;
    new = malloc(sizeof(listenelement));
    new -> value = v;
    new -> next = *l;
    *l = new;
}

//funktion zum Ausgeben der Liste
void print_list(list l){
    if (l==NULL){
        printf("Ende");
    }
    while (l!=NULL){
        printf("%d\n", l-> value);
        l = l->next;
    }
}

// funktion zum zählen der Listenelemente
int length(list l){
    int count = 0;
    while (l!=NULL){
        count = count + 1;
        l = l->next;
    }
    return count;
}

//funktion zum löschen des ersten (head) Elements
int delete_head(list*l){
    while (l != NULL) {
        if (*l == NULL){
            return -1;
        }
        list old = *l;
        *l = old->next;
        free(old);
        
    }
    return 0;
}

//funktion zum löschen aller elemente
void delete_all(list l){
    list next;
    while (l!=NULL){
        next = l->next;
        free(l);
        l=next;
    }
}

// Löscht element an position "pos"
int delete_pos(list * l, int pos){
    if (pos < 0 || pos > length(*l) || *l == NULL){			//falls Parameter pos außerhalb der Liste: Rückgabewert -1
        return -1;
    }
    if (pos == 0){											//falls Parameter pos auf 0
        *l = (*l)->next;
        return 0;
    }
    if(pos == 1){											//falls Parameter pos auf 1
        if( (*l)->next == NULL){
            free(l);
            return 0;
        }
        (*l)->next = (*l)->next->next;
        return 0;
    }
    list lakt = *l;											//Liste zwischenspeichern
    return delete_pos(&lakt -> next, pos -1);					//rekursiver Aufruf
}

// löscht erstes Element X aus Liste
int delete_element(list * l, int e){
    if ((*l) -> value == e){
        (*l) = (*l)->next;
        return 0;
    }
    list lakt = *l;											//Liste zwischenspeichern
    return delete_element(&lakt->next, e );					//rekursiver Aufruf
}

// sortiert die Liste je nach Parameter m aufsteigend oder aufsteigend mit den Werten in Betragsdarstellung
void sort(list * l, int m) {
	if (m > 0) {											//Parameter m ist positiv (aufsteigend sortieren) (eigentlicher Sortier-Algorithmus)
		int intCache = 0;									//Cache um aktuelles Element zwischenzuspeichern und zu vergleichen
		list poiNew = *l;									//Pointer auf aktuelles Element
		list poiLastVal = NULL;								//Pointer auf letztes Element
		while (poiNew != NULL) {							//Elemente so lange vergleichen bis Zeiger auf NULL steht
			poiLastVal = poiNew;
			poiNew = poiNew->next;
			if (poiNew == NULL) {							//Wenn alle Elemente verglichen, dann Speicher freigeben und Funktion verlassen
				free(poiNew);
				return;
			}
			else if (poiNew->value > poiLastVal->value) {	//falls aktueller Wert > leztzter Wert steht aktueller Wert an der richtigen Stelle, schleife von vorne
				continue;
			}
			else if (poiNew->value < poiLastVal->value) {	//falls aktueller Wert < letzter Wert müssen beide vertauscht werden
				intCache = poiNew->value;					//Tausch: Cache = A, A = B, B = Cache
				poiNew->value = poiLastVal->value;
				poiLastVal->value = intCache;
				sort(l, m);									//liste erneut von vorne durchgehen
			}
		}
	}
	else if (m < 0) {										//Parameter m ist negativ (Liste in Betragsform umwandeln)
		list listSort = *l;
		while (listSort != NULL) {							//Elemente in listSort so lange vergleichen bis der Zeiger auf NULL zeigt
			if (listSort->value > 0) {						//wenn Wert value positiv, Zeiger weiter setzen
				listSort = listSort->next;
				continue;
			}
			else if (listSort->value < 0) {					//wenn Wert value negativ, absoluten Wert nehmen und Zeiger weiter setzen
				listSort->value = abs(listSort->value);
				listSort = listSort->next;
			}
		}
		return sort(l, 1);									//Funktion erneut mit positivem Parameter in Betragsform erneut aufrufen
	}
	else {													//Fall Parameter = 0 (währe nicht definiert)
		printf("\nUngueltiger Parameter in sort()!");
	}
}

//Überprüft ob die Liste leer ist (eine leere Liste kann nicht sortiert werden!
void checkList(list * l) {									
	if (*l == NULL) {
		printf("Liste ist leer und kann nicht behandelt werden!");
		exit(EXIT_FAILURE);
	}
}

int main() {
    struct le *Liste;
	int value;
    Liste=NULL;
	insert(-7, &Liste);											//Elemente zur Liste hinzufügen
	insert(-3, &Liste);
    insert(1, &Liste);
    insert(4, &Liste);
    insert(6, &Liste);
    insert(2, &Liste);
    insert(5, &Liste);
    insert(7, &Liste);
    insert(9, &Liste);
	
	checkList(Liste);											//Überprüft ob die Liste Elemente enthält

    printf("\nListe roh: \n");
	print_list(Liste);											//Liste mit Elementen ausgeben									
	printf("\nListe aufsteigend sortiert (Parameter 1): \n");		
	sort(&Liste, 1);											//Liste aufsteigend sortieren
	print_list(Liste);											//Liste ausgeben
	printf("\nListe in Betragsform (Parameter -1): \n");
	sort(&Liste, -1);											//Liste in Betragsform aufsteigend sortieren
    print_list(Liste);											//Liste ausgeben
    printf("\nListe ohne 0tes Element: \n");
    delete_pos(&Liste, 0);										//Kopf der Liste (pos 0) löschen
	print_list(Liste);											//Liste ausgeben
    printf("\nListe ohne Element mit wert 4: \n");
    delete_element(&Liste, 4);									//Element mit Wert 4 löschen
    print_list(Liste);											//Liste ausgeben
    printf("\nListe geloescht: \n");
    delete_all(Liste);											//gesamte Liste löschen
    print_list(Liste);											//Liste ausgeben
    
    return 0;
}
