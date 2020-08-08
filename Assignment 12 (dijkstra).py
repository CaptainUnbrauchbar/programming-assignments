#Programming Assignment 12: Dijkstra 
# Name, Vorname: Frankreiter, Florian
# Matr.-Nr: 796762


def dijkstra(adjL,startNode,targetNode):
    pre = [None for i in range(len(adjL))]                      # Vorgänger
    distance = [float('inf') for i in range(len(adjL))]         # Distanzen
    distance[startNode] = 0                                     # Distanz zu Start = 0
    Q = [i for i in range(len(adjL))]                           # Liste von allen Knoten

    while len(Q) > 0:                                           # Dijkstra
        minDist = float('inf')                                  # Knoten mit minimaler Distanz der noch in Q ist ermitteln:
        for k in Q:                                             # Minimalen Wert finden (brute force sry)
            temp = distance[k]
            if minDist > temp:
                minDist = temp
                
        if minDist == float('inf'):                             # wenn kein Pfad möglich, inf zurückgeben
            return float('inf') 

        u = distance.index(minDist)                             # u ist nun Knoten mit minimaler Distanz
        Q.remove(u)                                             # u aus Q entfernen

        if u == targetNode:                                     # frühe Abbruchbedingung: Wenn Zielknoten bereits gefunden nicht weiter machen
            return distance[targetNode]
        for j in range(len(adjL[u])):                           # Nachbarn ermitteln
            v = adjL[u][j][0]                                   # Nachbar v
            if v in Q:                                          
                temp = distance[u] + adjL[u][j][1]              # Distanz aktualisieren wenn v in Q
                if temp < distance[v]:
                    distance[v] = temp
                    pre[v] = u
        
    return distance[targetNode]                                 

adjL=[[[1,1],[2,3]],[[3,6],[4,7]],[[3,2],[5,9]],[],[[5,4],[6,10]],[[6,8]],[]]
startNode=0
targetNode=6

print(dijkstra(adjL,startNode,targetNode))
