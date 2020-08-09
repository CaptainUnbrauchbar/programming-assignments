# Algorithmen und Datenstrukturen
# Programmieraufgabe 3 - Dijkstra, Kruskal
# Abgabedatum: 05.08.2019
#
# Gruppennummer: <40>
# Gruppenmitglieder: 
# - <Florian Frankreiter>
# - <Rafael Vicaria Barker>
# - <Fabian Lyszio>

## ACHTUNG: Verwenden Sie fuer Ihre Kommentare nur ein einzelnes #-Zeichen:
# so sollte Ihr Kommentar markiert werden
## so sind die Kommentare aus der Aufgabenstellung markiert.

import copy, math

## Implementieren Sie ab hier Ihre Loesungen:
def dijkstra(g, s):
    ## hier soll Ihre Implementierung stehen.

    knoten, dist, pre, nachbarn, distCp, result = [], [], [], [], [], []

    u = s-1
    li = len(g)

    for v in range(li):
        dist.append(math.inf)       # Distanzen am Anfang auf unendlich setzen
        pre.append(None)            # Vorgänger Knoten auf none setzen
        knoten.append(v)            # Knoten liste besteht nun aus werten 0 - len(g)-1 (0, 1, 2, 3, 4...) und wird später als Queue benutzt
        distCp.append(None)         # distCp wird später tiefe kopie von dist
    dist[u] = 0                     # distanz zum Startknoten u = s-1 ist 0

    distCp = copy.deepcopy(dist)    # erstelle tiefe kopie von dist
    
    while len(knoten) > 0:
        indexMinDist = distCp.index(min(distCp))    # finde index von kleinstem wert in dist
        u = knoten.pop(indexMinDist)                # u ist knoten mit kleinster Distanz, Knoten wird entfernt da besucht
        distCp.pop(indexMinDist)                    # die indizes von distcp müssen immer synchron zu denen in Knoten bleiben

        for i in range(li):                         # finde alle Nachbarn vom aktuellen Knoten
            if (g[u][i]) != -1:
                nachbarn.append(i)                  # nachbarn enthält nun die Indizes der Nachbarknoten

        for v in nachbarn:                          # für alle Nachbarn
            if v in knoten:                         # wenn Nachbarknoten noch nicht besucht wurde
                newdist = dist[u] + g[u][v]         # newdist ist totale distanz von Startknoten zu Nachbarn (dist zu aktuellem Knoten + dist von aktuellem Knoten zu Nachbarn)
                if newdist < dist[v]:               # wenn neu berechnete Distanz kleiner als alte Distanz
                    dist[v] = newdist               # ersetze durch kleinere Distanz
                    pre[v] = u                      # lege Vorgängerknoten fest um den Pfad wieder zu finden
                    nachbarn = []                   # Nachbarn wird geleert da verarbeitet
    
    for i in range(li):                 # die liste pre wird in die jeweiligen Pfade übersetzt
        result.append([])               # Zeile erstellen
        result[i].append(i+1)           # Zeile mit Zielknoten füllen
        u = i                           # u ist aktueller Zielknoten
        while pre[u] != None:           # pre von Startknoten ist none, ende des aktuellen Pfades
            u = pre[u]                  # u wird so lange zum Vorgänger von u bis Startknoten none gefunden ist
            result[i].insert(0, u+1)    # alle u direkt links in der aktuellen Zeile einfügen
        
    return result

def kruskal(g):
    ## hier soll Ihre Implementierung stehen.

    result, L, v, visited, knoten = [[-1 for i in range(len(g))] for j in range(len(g))], [], [], [], []

    for i in range(len(g)):                                         # Liste L mit Kantengewichten erstellen
        for j in range(len(g)):
            if g[i][j] != -1 and g[i][j] not in L:                  # Alle Werte die nicht -1 sind in L eintragen
                L.append(g[i][j])
    L.sort()                                                        # L aufsteigend sortieren (greedy)
    
    for k in L:                                                     # Liste v mit allen kanten erstellen (in Bezug auf L)
        for i, cache in enumerate(g):                               
            if k in cache and [cache.index(k)+1, i+1] not in v:     
                v.append([i+1, cache.index(k)+1])                   
                                                                    # v ist nun nach L sortiert aufgestellt
    for i in range(len(v)): 
        visited.append(False)                                       # Hilfslisten visited und knoten für Prüfung auf Kreise im Graphen
        knoten.append(i+1)

    u = v[0][0]                                         # Startelement
    visited[u] = True                                   

    kreisGefunden = False
    for i in range(len(v)):
        k = v[i][0]                                     
        u = v[i][1]     
        if visited[u]:                                  # wenn u bereits besucht
            for j in range(len(g)+1):                   
                if [u, j] in v:                         # prüfe ob es von u weitere kanten gibt
                    if visited[u] and visited[j]:       # wenn es die Knoten der weiteren Kante bereits besucht wurden gibt es einen Kreis
                        kreisGefunden = True            
                        v[i] = [-1, -1]                 # Knoten wird nicht gelöscht, da indizes nicht verschoben werden dürfen
                        break                           
            if not kreisGefunden:                       # falls doch kein Kreis gefunden wie normal weiter machen
                visited[k] = True                       # Knoten der Kante auf besucht setzen
                visited[u] = True
        else:
            visited[k] = True                           # Knoten der Kante auf besucht setzen
            visited[u] = True
               
    for i in range(len(g)):                         # nachdem alle Kanten die Kreise bilden auf [-1, -1] gesetzt wurden:
        if v[i] != [-1, -1]:                        # alle Knoten die keine Kreise bilden in result übersetzen
            result[v[i][0]-1][v[i][1]-1] = L[i]     # result bekommt an den jeweiligen Indizes die Kantengewichte aus L
            result[v[i][1]-1][v[i][0]-1] = L[i]     # gespiegelt an der Hauptdiagonalen

    return result

def pathCosts(l, z, g):
    ## hier soll Ihre Implementierung stehen.
    u = z-1
    result = 0

    for k in range(len(l[u])-1):    
        i = l[u][k] - 1             # Es werden jeweils 2 aufeinanderfolgende Knoten aus l genommen
        j = l[u][k+1] - 1           # und in i, j abgelegt; -1 da Listen bei 0 anfangen.
        result += g[i][j]           # In der Adjazenzliste sind die Wegkosten von i nach j an g[i][j] abgelegt.
                                    # Diese werden so oft zu result addiert wie man Kanten 'überschreitet'
    return result

def spanTreeWeight(a):
    ## hier soll Ihre Implementierung stehen.
    result = 0
    for i in range(len(a)):         # Für Spannbaumgewicht alle Kantengewichte zusammenaddieren (nested for loops -> brute force)
        for j in range(len(a[0])):
            if a[i][j] != -1:
                result += a[i][j]

    result = result // 2            # Wegen Hauptdiagonale durch 2 Teilen
    return result

## Hier ist ein Testfall:

print('\n+++ Dijkstra Test: von 4 zu 2 +++')
dgraph = [
    [-1,  3, -1, -1, -1, -1, -1],
    [ 1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [ 4,  9,  5, -1,  2, -1, -1],
    [-1, -1, -1, 17, -1, 12,  8],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1]]

dresult = dijkstra(dgraph, 4)
print(dresult)
costs = pathCosts(dresult, 2, dgraph)

print('Kosten:')
print(costs) ## 7

print('\n+++ Kruskal Test +++')
kgraph = [
    [-1, 19, 25, 20, 12,  8],
    [19, -1,  5, -1, -1, 16],
    [25,  5, -1,  7, -1, -1],
    [20, -1,  7, -1, -1, 30],
    [12, -1, -1, -1, -1, 10],
    [ 8, 16, -1, 30, 10, -1]]

kresult = kruskal(kgraph)
print(kresult)
weight = spanTreeWeight(kresult)

print('Gewicht:')
print(weight) ## 46

## Dies soll die letzte Zeile in der Datei sein.