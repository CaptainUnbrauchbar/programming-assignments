#Programming Assignment 11: Dynamic Programming 
# Name, Vorname: Frankreiter, Florian
# Matr.-Nr: 796762

def NChooseK(n,k):
    if k > n:
        return [0,0,0]                                              # Yes :)
    
    pascal = [[1] for i in range(n+1)]                              # Listenstruktur für Pascalsches Dreieck erzeugen
    if n > 0:
        pascal[1].append(1)

    for j in range(2,n+1):                                          # Pascalsches Dreieck füllen
        for l in range(0,j-1):
            pascal[j].append(pascal[j-1][l] + pascal[j-1][l+1])
        pascal[j].append(1)
    
    erg = pascal[n][k]                                              # Ergebnis auslesen
    for i in range(k+1,n+1):                                        # Einträge die nach Ergebnis kommen für Zählen löschen
        pascal[n].pop(k+1)

    gerade = 0
    ungerade = 0

    for x in pascal:                                                # Zählen
        for y in x:
            if y % 2 == 0:
                gerade += 1
            if y % 2 != 0:
                ungerade += 1

    return [erg, gerade, ungerade]                                  # Liste zurückgeben

if __name__ == '__main__':
    print(NChooseK(6,4))
    print(NChooseK(10,1))
    print(NChooseK(5,3))
    print(NChooseK(0,0))
    print(NChooseK(5,0))
    print(NChooseK(15,15))
    print(NChooseK(4,10))
    print(NChooseK(100,99))
    print(NChooseK(100,98))
    #print(NChooseK(100000,99999))   #rip ram