#Programming Assignment 13: Kruskal
# Name, Vorname: Frankreiter, Florian
# Matr.-Nr: 796762

def make_set(V):                # make-set(v)
    V.append([len(V)])
    return V                    # gibt V mit einem zusätzlichen Knoten zurück

def union(V,r,s):               # zwei Knoten zu Teilgraph vereinigen
    for i in range(len(V)):     # liste mit r und s finden
        if r in V[i]:
            r = i
        if s in V[i]:
            s = i

    for i in range(len(V[s])):
        V[r].append(V[s][i])
    V.pop(s)
    return V                    # gibt V mit vereinigten Knoten zurück

def find(V,r):                  # zum prüfen ob 2 Knoten im selben Teilgraph/Liste sind
    for i in range(len(V)):
        if r in V[i]:
            return i            # gibt index des "Teilgraphen" in V zurück
    return "nicht in V"         # wenn Knoten nicht in V
    

def kruskal(adjM):
    if len(adjM) == 0:
        return 0
    E = []                                                      # Liste aller Kanten
    for i in range(0,len(adjM)):                                # Ordne Kanten e_1, e_2, ..., e_n aufsteigend zu [w,u,v]
        for j in range(i+1,len(adjM)):                          # nur oberhalb der Hauptdiagonalen auswerten
            if adjM[i][j] != 0:                                 # wenn Kante vorhanden:
                temp = adjM[i][j]
                if len(E) == 0:                                 # bei leerer Liste einfach einfügen
                    E.append([adjM[i][j],i,j])                  # einfügen [w,u,v]
                else:                                           # ansonsten sortiert einfügen
                    for k in range(len(E)):
                        if temp <= E[k][0]:
                            E.insert(k,[adjM[i][j],i,j])        # einfügen [w,u,v]
                            break
                        if k == len(E)-1:
                            E.append([adjM[i][j],i,j])          # einfügen [w,u,v]
                            
    V = []                                      # Liste aller Knoten
    for x in range(len(adjM)):  
        make_set(V)                             # Knoten einfügen
    Eerg = []                                   # Liste für min. Spannbaum

    for y in range(len(E)):                     # <KRUSKAL> in Reihenfolge der sortierten Kanten in E
        if find(V,E[y][1]) != find(V,E[y][2]):  # wenn kleinster Knoten nicht in Teilgraph
            union(V,E[y][1],E[y][2])            # Kante zu Teilgraph hinzufügen
            Eerg.append(E[y])                   # Kante in min. Spannbaum einfügen

    minSpannbaumCost = 0
    for z in range(len(Eerg)):                  # min. Spannbaum auswerten und Gewichte zusammenzählen
        minSpannbaumCost += Eerg[z][0]  

    return minSpannbaumCost                     # Gewicht des min. Spannbaums ausgeben

adjM=[
[0, 3, 0, 0],
[3, 0, 5, 0],
[0, 5, 0, 0],
[0, 0, 0, 0]]
print(kruskal(adjM))

adjM=[
[0, 3, 5, 8, 0, 0, 0],
[3, 0, 0,10, 0, 0, 0],
[5, 0, 0, 7,14, 0, 0],
[8,10, 7, 0, 0, 3, 0],
[0, 0,14, 0, 0,17, 4],
[0, 0, 0, 3,17, 0, 2],
[0, 0, 0, 0, 4, 2, 0]]
print(kruskal(adjM))

adjM=[]
print(kruskal(adjM))

adjM=[
[0,2],
[2,0]]
print(kruskal(adjM))

adjM=[
[0, 2, 5, 0, 0, 0, 0, 7, 1], 
[2, 0, 1, 10, 4, 5, 5, 0, 0], 
[5, 1, 0, 0, 0, 122, 0, 0, 12], 
[0, 10, 0, 0, 22, 2, 0, 0, 0], 
[0, 4, 0, 22, 0, 0, 0, 0, 0], 
[0, 5, 122, 2, 0, 0, 0, 0, 0], 
[0, 5, 0, 0, 0, 0, 0, 6, 122], 
[7, 0, 0, 0, 0, 0, 6, 0, 0], 
[1, 0, 12, 0, 0, 0, 122, 0, 0]]
print(kruskal(adjM))

adjM=[
[0, 2, 5, 0, 0, 0, 0, 7, 1], 
[2, 0, 1, 10, 4, 5, 5, 0, 0], 
[5, 1, 0, 0, 4, 122, 0, 0, 12], 
[0, 10, 0, 0, 22, 2, 0, 0, 9], 
[0, 4, 4, 22, 0, 2, 13, 4, 0], 
[0, 5, 122, 2, 2, 0, 0, 0, 0], 
[0, 5, 0, 0, 13, 0, 0, 6, 122], 
[7, 0, 0, 0, 4, 0, 6, 0, 5], 
[1, 0, 12, 9, 0, 0, 122, 5, 0]]
print(kruskal(adjM))

adjM=[
[0, 2, 5, 0, 0, 0, 0, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[2, 0, 1, 10, 4, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[5, 1, 0, 0, 4, 122, 0, 0, 12, 1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 10, 0, 0, 22, 2, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 4, 4, 22, 0, 2, 13, 4, 0, 0, 0, 0, 0, 0, 0, 22, 2, 0, 0, 0], 
[0, 5, 122, 2, 2, 0, 0, 0, 0, 0, 1, 0, 113, 13, 0, 0, 0, 0, 0, 0], 
[0, 5, 0, 0, 13, 0, 0, 6, 122, 0, 0, 0, 0, 0, 0, 0, 9, 3, 0, 0], 
[7, 0, 0, 0, 4, 0, 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[1, 0, 12, 9, 0, 0, 122, 5, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 1, 0, 0, 0, 0, 0, 9, 0, 13, 0, 0, 0, 0, 0, 0, 0, 9, 0], 
[0, 0, 0, 0, 0, 1, 0, 0, 0, 13, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 113, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 9, 0, 0, 0, 0], 
[0, 0, 0, 0, 22, 0, 0, 0, 0, 0, 0, 0, 0, 2, 9, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 2, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 4, 0, 1], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
print(kruskal(adjM))