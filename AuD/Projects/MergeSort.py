# Algorithmen und Datenstrukturen
# Programmieraufgabe 2 - Sortierverfahren
# Abgabedatum: 07.07.2019
#
# Gruppennummer: <40>
# Gruppenmitglieder: 
# - <Florian Frankreiter>
# - <Rafael Vicaria Barker>
# - <Fabian Lyszio>

# Implementieren Sie ab hier Ihre Lösungen:

# Enum Klasse importieren
from enum import Enum

istFertig = 0

# Enum Klasse
class Animal(Enum):
	Ameise=1
	Maus=2
	Hamster=3
	Katze=4
	Hund=5
	Panda=6
	Pferd=7
	Nashorn=8
	Elefant=9
	Blauwal=10

# MERGESORT CODE

# Funktion Merge um die Listen links, rechts zu mischen (Aufruf in mergeSort)
def merge(links, rechts):
	global istFertig
	cache = []										# Neue Liste die später das Ergebnis enthält, wird bei Aufruf automatisch geleert
	strL = ""
	strR = ""

	for n in range(len(links)):						# zu String umwandeln um die Zwischenschritte auszugeben (kein Teil vom Algorithmus)	
		strL += " "									
		strL += links[n]
	for m in range(len(links)):						# zu String umwandeln um die Zwischenschritte auszugeben (kein Teil vom Algorithmus)
		strR += " "
		strR += rechts[m]

	print("\n Zu mischen (L, R):%s, %s\n" % (strL, strR))

	while len(links) > 0 and len(rechts) > 0:													# Solange die beiden Listen nicht leer sind:
																								# Die ersten Elemente der beiden Listen werden mit Hilfe der Member-Werte in der Enum Klasse verglichen:
		if Animal[links[0]].value <= Animal[rechts[0]].value:									# Falls erstes Element links <= erstes Element rechts:
			print(" %s ist kleiner als %s!" % (links[0], rechts[0]))
			print(" %s wird aus Links entfernt und in Cache hinten eingefügt!" % (links[0]))
			cache.append(links.pop(0))															# erstes Element links wird in cache hinten eingefügt und aus links gelöscht
			print(" Cache: %s\n" % (cache))
		else:																					# Falls erstes Element links > erstes Element rechts:
			print(" %s ist kleiner als %s!" % (rechts[0], links[0]))
			print(" %s wird aus Rechts entfernt und in Cache hinten eingefügt!" % (rechts[0]))
			cache.append(rechts.pop(0))															# erstes Element rechts wird in cache hinten eingefügt und aus rechts gelöscht
			print(" Cache: %s\n" % (cache))
																		# Restliche Elemente anfügen (erstes Element bereits verglichen): 
	while len(links) > 0:                                               # Solange links nicht leer:
		print(" %s wird hinten an Cache angefügt!\n" % (links[0]))
		cache.append(links.pop(0))                                      # 'neues erstes' Element links wird in cache hinten eingefügt und aus links gelöscht
		print(" Cache: %s\n" % (cache))

	while len(rechts) > 0:                                              # Solange rechts nicht leer:
		print(" %s wird hinten an Cache angefügt!\n" % (rechts[0]))
		cache.append(rechts.pop(0))                                     # 'neues erstes' Element rechts wird in cache hinten eingefügt und aus rechts gelöscht
		print(" Cache: %s\n" % (cache))

	if len(cache) == istFertig:
		print(" --- Sortieren fertig, Cache wird zurück gegeben! --- \n")
	else:
		print(" --- Links oder Rechts ist leer: Neuer Aufruf! --- \n")

	return cache                                                        # cache ist jetzt die aufsteigend Sortierte Liste und wird zurück gegeben

# Rekursive Funktion mergeSort um die Listen zu teilen
def mergeSort(L):
	strL = ""
	strR = ""

	if len(L) <= 1:                     # Basisfall Liste enthält ein oder kein Element únd Rekursionsende:
		return L                        # Liste muss nicht sortiert werden
	else:                               # Kein Basisfall:
		a = len(L) // 2                 # a markiert die Mitte der Liste L

		links = L[:a]
		for n in range(len(links)):		# zu String umwandeln um die Zwischenschritte auszugeben (kein Teil vom Algorithmus)
			strL += " "
			strL += links[n]
		print(" +++ Links:%s" % (strL))
		links = mergeSort(links)        # Liste Slicen: 0 bis Mitte

		rechts = L[a:]
		for n in range(len(links)):		# zu String umwandeln um die Zwischenschritte auszugeben (kein Teil vom Algorithmus)
			strR += " "
			strR += rechts[n]
		print(" +++ Rechts:%s" % (strR))
		rechts = mergeSort(rechts)      # Liste Slicen: Mitte bis Ende

		return merge(links, rechts)     # Rekursiver Aufruf merge um die aktuellen Listen links, rechts zu 'mischen' (Vorlesung 5)


# HEAPSORT CODE

# Funktion chg (Vorlesung 7)
def chg(L,i,j):							# Tauscht L[i] und L[j]
	tmp = L[i]							
	L[i] = L[j]							
	L[j] = tmp
	
# Funktion heapify absteigend (teilweise Vorlesung 7)
def heapify(L,v,last):
	w = 2 * v + 1												# linkes kind von v
	while (w <= last):											# Knoten 'w' abarbeiten
		if (w+1 <= last):										# existiert ein rechtes kind? 
			if (Animal[L[w]].value > Animal[L[w+1]].value):		# w = child mit größtem Element
				 w = w+1	
		if (Animal[L[v]].value <= Animal[L[w]].value):			# Heapeigenschaft -> Ende
			 return
		chg(L,v,w)
		v = w
		w = 2 * v + 1

# Funktion buildHeap (Vorlesung 7)
def buildHeap(L):
	last = len(L) - 1								# für alle inneren Knoten bottom-up
	for v in range((last-1)//2,-1,-1):				# Heapeigenschaft wieder herstellen
		heapify(L,v,last)

# Funktion buildHeap (Vorlesung 7)
def heapSort(L):
	it = 0											# Zähler für Ausgabe (kein Teil des Algorithmus)
	buildHeap(L)
	print("Aufbau Heap:    %s" % (L))
	last = len(L) -1
	while (last >= 1):								# Anfangsknoten tauschen
		it += 1										# Zähler für Ausgabe (kein Teil des Algorithmus)
		chg(L,last,0)								# 'last' Knoten aus Baum entfernen
		last = last - 1								# Heapeigenschaft wieder herstellen
		heapify(L,0,last)
		print("Sortierdurchlauf %s: %s" % (it, L))		
	return L

# Hier ist ein Testfall:
L=["Panda","Ameise","Nashorn","Pferd","Blauwal","Katze","Hund","Maus","Panda"]
istFertig = len(L)

print("######MERGESORT######")
print("\nMergesort, Parameter L: %s\n" % (L))
print("\nMergeSort, Sortiert: %s\n" % (mergeSort(L)))

print("\n\n\n\n######HEAPSORT######")
print("\nHeapsort, Parameter L: %s\n" % (L))
print("\nHeapSort, Sortiert: %s\n" % (heapSort(L)))

# Das Ergebnis sollten folgende Liste sein:
# ['Ameise', 'Maus', 'Katze', 'Hund', 'Panda', 'Panda', 'Pferd', 'Nashorn', 'Blauwal']
# ['Blauwal', 'Nashorn', 'Pferd', 'Panda', 'Panda', 'Hund', 'Katze', 'Maus', 'Ameise']