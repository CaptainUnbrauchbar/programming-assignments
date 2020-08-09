# Algorithmen und Datenstrukturen
# Hausaufgabe 1 - Matrizenmultiplikation
# Abgabedatum: 2.6.2019
#
# Gruppennummer: <40>
# Gruppenmitglieder: 
# - <Florian Frankreiter>
# - <Rafael Vicaria Barker>
# - <Fabian Lyszio>

import copy
import math

# Diese Funktion können Sie verwenden, um Matrizen auszugeben.

def showMatrix(m):
    for line in m:
        print('|', end='')
        i = 0
        for value in line:
            if (i > 0):
                print(' ', end='')
            print(value, end='')
            i = i + 1
        print("|")

# Implementieren Sie ab hier Ihre Lösungen:

def matMultDef(a, b):			# Die Funktion Multipliziert A und B nach Definition in der Vorlesung!
	
	print(" \n+++ Multiplikation nach Definition +++\n")
	print(' Parameter a:')
	showMatrix(a)
	print('\n Parameter b:')
	showMatrix(b)

	checkvalue = matCheck(a,b)				# Es wird überprüft ob a und b multiplizierbar sind!
	if checkvalue == 1:						# n von a und m von b müssen gleich sein!
		print("\n ++ Die Multiplikation A * B ist nicht definiert (n von a != m von b)! ++ \n")
		exit(1)								# Exit with Error!

	# m x n a
	ma = len(a)										# Anzahl Zeilen a ermitteln
	na = len(a[0])									# Anzahl Spalten a ermitteln
	# m x n b
	mb = len(b)										# Anzahl Zeilen b ermitteln
	nb = len(b[0])									# Anzahl Spalten b ermitteln
	result = []		
	
	
	for x in range(ma):								# Leere m x n Matrix anlegen in die reingeschrieben werden kann!
		result.append([])							# "Zeilen" anlegen
		for y in range(nb):
			result[x].append(0)						# "Zeilen" mit "Spalten"/"Werten" füllen

													# Leere Liste ausgeben (Debugging)
	print("\n Rechenweg nach Definition: ")
	

	# Für Werte in Zeile i von a					# !!! Die Rechenschritte werden jeweils mit Print Befehlen ausgegeben !!!
	for i in range(ma):
		# Für Werte in Spalte j von b
		for j in range(nb):
			# Für Werte in Zeile k von b
			for k in range(mb):
				if (k <= ma and k > 0):
					print(" +\n")													# + Zeichen zwischen Multiplikationen
				else:
					showMatrix(result)												#Zwischenergebnis ausgeben
					print("______________________\n")								#Trennstrich zwischen den Rechnungen der einzelnen Elemente des Ergebnisses
				print("c", i+1, j+1, " = ", "a", i+1, k+1, "* b", k+1, j+1, "\n")	#Dokumentation der einzelnen Schritte über print			
				result[i][j] += a[i][k] * b[k][j]									#Einzelne Felder miteinander Multiplizieren, Addieren
				
	return result

def matMult(a, b):			# Identisch mit matMultDef, nur ohne print Ausgaben nach jedem Rechenschritt (für Strassen angelegt)

	# m x n a
	ma = len(a)										# Anzahl Zeilen a ermitteln
	na = len(a[0])									# Anzahl Spalten a ermitteln
	# m x n b
	mb = len(b)										# Anzahl Zeilen b ermitteln
	nb = len(b[0])									# Anzahl Spalten b ermitteln
	result = []		
	
	for x in range(ma):								# Leere m x n Matrix anlegen in die reingeschrieben werden kann!
		result.append([])							# "Zeilen" anlegen
		for y in range(nb):
			result[x].append(0)						# "Zeilen" mit "Spalten"/"Werten" füllen

	# Für Werte in Zeile i von a					# !!! Die Rechenschritte werden jeweils mit Print Befehlen ausgegeben !!!
	for i in range(ma):
		# Für Werte in Spalte j von b
		for j in range(nb):
			# Für Werte in Zeile k von b
			for k in range(mb):																							
				result[i][j] += a[i][k] * b[k][j]			#Einzelne Felder miteinander Multiplizieren, Addieren			
					
	return result

def matAdd(a, b):				# Die Funktion addiert A + B
	result = []
	for i in range(len(a)):	
		cache = []
		for j in range(len(a[0])):
			cache.append(a[i][j] + b[i][j])		# Element Axx aus A wird mit Element Bxx aus B addiert
		result.append(cache)
	return result

def matSub(a, b):				# Die Funktion subtrahiert A - B
	result = []
	for i in range(len(a)):
		cache = []
		for j in range(len(a[0])):
			cache.append(a[i][j] - b[i][j])		# Element Axx aus A wird mit Element Bxx aus B subtrahiert
		result.append(cache)
	return result

def matCheck(a, b):				# Die FUnktion matCheck überprüft ob die Multiplikation A * B definiert ist!

	# m x n a
	ma = len(a)						# Anzahl Zeilen a ermitteln
	na = len(a[0])					# Anzahl Spalten a ermitteln
	# m x n b
	mb = len(b)						# Anzahl Zeilen b ermitteln
	nb = len(b[0])					# Anzahl Spalten b ermitteln

	if na == mb:					# Anzahl Spalten A == Zeilen B?
		return 0					# 0 steht für kein Fehler!
	else:							# 1 steht für Fehler!
		return 1					

def matFillZero(a, size):		# Die Funktion füllt die Matrix a mit Nullen auf size x size auf!
	
	cache = []
	
	for x in range(size):					# Leere m x n Matrix sizexsize erstellen
		cache.append([])					# "Zeilen" anlegen
		for y in range(size):
			cache[x].append(0)				# "Zeilen" mit "Spalten"/"Werten" füllen
	
	# m x n
	ma = len(a)					# Anzahl Zeilen ermitteln
	na = len(a[0])				# Anzahl Spalten ermitteln
	
	for x1 in range(ma):		
		for x2 in range(na):	
			cache[x1][x2] = a[x1][x2]	
					
	a = copy.deepcopy(cache)	#Einzige Methode die nicht nur die Referenz übergeben hat...
	
	return a

def reduceZero(a, m, n):		# Die Funktion reduziert die Ergebnismatrix auf m x n und entfernt so überflüssige Nullen

	cache = []

	for x in range(m):						# Leere m x n Matrix sizexsize erstellen
		cache.append([])					# "Zeilen" anlegen
		for y in range(n):
			cache[x].append(0)				# "Zeilen" mit "Spalten"/"Werten" füllen

	for x1 in range(m):						# Werte werden in cache kopiert
		for x2 in range(n):	
			cache[x1][x2] = a[x1][x2]	

	return cache
	
def matMultSA(a, b):		# Matrix Multiplikation nach Strassen (iterativ)
	
	print(" \n+++ Multiplikation nach Strassen +++\n")
	print(' Parameter a:')
	showMatrix(a)
	print(' \n Parameter b:')
	showMatrix(b)				
	
	checkvalue = matCheck(a,b)				# Es wird überprüft ob a und b multiplizierbar sind!
	if checkvalue == 1:						# n von a und m von b müssen gleich sein!
		print("\n ++ Die Multiplikation A * B ist nicht definiert (n von a != m von b)! ++ \n")
		exit(1)								# Exit with Error!

	# Von Anfang an werden 2 Dimensionale Listen erstellt (Einfacher als diese manuell zu befüllen)

	# ++ Ab hier werden Listen initialisiert ++

	a11 = [[0 for x in range(1)] for y in range(1)]				
	a12 = [[0 for x in range(1)] for y in range(1)]
	a21 = [[0 for x in range(1)] for y in range(1)]
	a22 = [[0 for x in range(1)] for y in range(1)]

	b11 = [[0 for x in range(1)] for y in range(1)]
	b12 = [[0 for x in range(1)] for y in range(1)]
	b21 = [[0 for x in range(1)] for y in range(1)]
	b22 = [[0 for x in range(1)] for y in range(1)]
	
	c11 = [[0 for x in range(1)] for y in range(1)]
	c12 = [[0 for x in range(1)] for y in range(1)]
	c21 = [[0 for x in range(1)] for y in range(1)]
	c22 = [[0 for x in range(1)] for y in range(1)]
	
	Cache1 = []
	Cache2 = []
	
	result = [[0 for x in range(1)] for y in range(1)]
	
	# ++ Bis hier werden Listen initisalisiert ++
	
	# fillSize ist die größte Zweierpotenz nach x und bestimmt wie weit a und b mit Nullen aufgefüllt werden!

	varmax = max(max(len(a),len(a[0])),max(len(b),len(b[0])))	# Beide m und n von A und B werden verglichen und der größte Wert wird in varmax gespeichert
	fillSize = 2**(math.ceil(math.log2(varmax)))				# Die nächste 2er Potenz nach varmax wird ermittelt (2^runden(log2(x))
																# log2(x) wird gerundet und danach in 2^x potenziert

	rSizeM = len(a)												# Voraussichtliche Größe des Ergebnisses zwischenspeichern (Um später überflussige Nullen zu entfernen)
	rSizeN = len(b[0])

	a = matFillZero(a, fillSize)			# a und b mit Nullen auffüllen!
	b = matFillZero(b, fillSize)

	# m x n b	
	ma = len(a)						# Anzahl Zeilen ermitteln
	na = len(a[0])					# Anzahl Spalten ermitteln
	mb = len(b)						# Anzahl Zeilen b ermitteln
	nb = len(b[0])					# Anzahl Spalten b ermitteln	

	# Die Matrizen A und B werden erneut ausgegeben

	print("\n ______________________")
	print("\n Die Matrix A wurde mit Nullen auf", ma, "x", na, "aufgefüllt: ")
	showMatrix(a)
	print("\n Die Matrix B wurde mit Nullen auf", mb, "x", mb, "aufgefüllt: ")
	showMatrix(b)
	
	# Die Sub-Matrizen werden auf m/2 x n/2 erweitert und befüllt

	a11 = matFillZero(a11, ma//2)
	a12 = matFillZero(a12, ma//2)
	a21 = matFillZero(a21, ma//2)
	a22 = matFillZero(a22, ma//2)
	
	b11 = matFillZero(b11, mb//2)
	b12 = matFillZero(b12, mb//2)
	b21 = matFillZero(b21, mb//2)
	b22 = matFillZero(b22, mb//2)
			
	# Routine um die Sub-Matrizen mit den Werten aus a und b zu befüllen

	for x1 in range(ma//2): 
		for x2 in range(na//2):	
			a11[x1][x2] = a[x1][x2] 
			b11[x1][x2] = b[x1][x2] 
	for x1 in range(ma//2): 
		for x2 in range(na//2, na): 
			e2 = x2-na//2
			a12[x1][e2] = a[x1][x2] 
			b12[x1][e2] = b[x1][x2]	
	for x1 in range(ma//2, ma): 
		for x2 in range(na//2): 
			e1 = x1-ma//2
			a21[e1][x2] = a[x1][x2] 
			b21[e1][x2] = b[x1][x2] 
	for x1 in range(ma//2, ma): 
		for x2 in range(na//2, na):	 

			e1 = x1-ma//2	

			e2 = x1-na//2						
			a22[e1][e2] = a[x1][x2] 
			b22[e1][e2] = b[x1][x2] 
	
	# Die Vollbrachte Zerlegung in 4 Sub-Matrizen wird mit Print-Direktiven Dokumentiert:

	print("\n ______________________")
	print("\n Die Matrix A wurde in a11-a22 zerlegt: ")
	print("\n a11: ")
	showMatrix(a11)
	print(" a12: ")
	showMatrix(a12)
	print(" a21: ")
	showMatrix(a11)
	print(" a22: ")
	showMatrix(a11)

	print("\n ______________________")
	print("\n Die Matrix B wurde in b11-b22 zerlegt: ")
	print("\n b11: ")
	showMatrix(b11)
	print(" b12: ")
	showMatrix(b12)
	print(" b21: ")
	showMatrix(b21)
	print(" b22: ")
	showMatrix(b22)

	# M1 - M7 werden berechnet (Rechenweg von Wikipedia)
	# Mit Print-Ausgaben um den Rechenweg zu Dokumentieren

	print("\n ______________________")
	print("\n M1-M7 werden berechnet: ")

	M1 = matMult(matAdd(a11,a22),matAdd(b11,b22))	# M1 = (A11 + A22) * (B11 + B22)
	print("\n M1:")
	showMatrix(M1)

	M2 = matMult(matAdd(a21,a22),b11)				# M2 = (A21 + A22) * B11
	print("\n M2:")
	showMatrix(M2)

	M3 = matMult(a11,matSub(b12,b22))				# M3 = A11 * (B12 - B22)
	print("\n M3:")
	showMatrix(M3)

	M4 = matMult(a22,matSub(b21,b11))				# M4 = A22 * (B21 - B11)
	print("\n M4:")
	showMatrix(M4)

	M5 = matMult(matAdd(a11,a12),b22)				# M5 = (A11 + A12) * B22
	print("\n M5:")
	showMatrix(M5)

	M6 = matMult(matSub(a21,a11),matAdd(b11,b12))	# M6 = (A21 - A11) * (B11 + B12)
	print("\n M6:")
	showMatrix(M6)

	M7 = matMult(matSub(a12,a22),matAdd(b21,b22))	# M7 = (A12 - A22) * (B21 + B22)
	print("\n M7:")
	showMatrix(M7)

	# M1 - M7 werden Zusammengefügt und in c11-c22 gespeichert (Rechenweg von Wikipedia)
	# Erneut werden Cache1 und Cache2 für Zwischenergebnisse verwendet!

	print("\n ______________________")
	print("\n M1-M7 werden zum Endergebnis zusammengerechnet....\n ")

	c11 = matAdd(matSub(matAdd(M1,M4),M5),M7)
	c12 = matAdd(M3,M5)
	c21 = matAdd(M2,M4)
	c22 = matAdd(matSub(M1,M2),matAdd(M3,M6))

	Cache1 = c11+c21
	Cache2 = c12+c22
		
	result = matFillZero(result, fillSize)		#Result wird mit Nullen aufgefüllt
	
	#Cache1 und Cache2 werden zu Result zusammengefügt (Elementweise)
	
	for x1 in range(ma):
		for x2 in range(na//2):
			result[x1][x2] = Cache1[x1][x2]
	
	for x1 in range(ma):
		for x2 in range(na//2, na):
			e2 = x2-na//2
			result[x1][x2] = Cache2[x1][e2]		
	
	showMatrix(result)	
	print("\n Überflussige Nullen werden reduziert....")

	result = reduceZero(result, rSizeM, rSizeN)		#Überflüssige Nullen aus Ergebnis entfernen!
		
	return result
 
# -------------------------------------------------------

# Testfall:
# a =
# |3 2 1|
# |1 0 2|

# b =
# |1 2|
# |0 1|
# |4 0|

# Das Ergebnis sollte folgende Matrix sein:
# a * b =
# result =
# |7 8|
# |9 2|

# Vorgegebens Beispiel: 2x3 * 3x2 = 2x2
a,b = [[3, 2, 1],[1, 0, 2]], [[1, 2],[0, 1],[4, 0]]		#Lsg: (7,8) (9,2)

# Eigene Beispiele zum Testen und Ausnahmenbehandlung Testen: (Kommazahlen, Negative Eingaben, Sehr große Eingaben, Nicht Definiert...)

# ++ Von Hand auskommentieren je nachdem was benötigt wird ++

# Beispiel mit Werten mit Nachkommastellen 2x3 * 3x2 = 2x2
#a,b = [[3.52, 2, 1.6],[1, 0.42, 2]], [[1, 2.23],[0, 1],[4.25, 0]]

# Zweites Beispiel zum Testen: 4x3 * 3x3 = 4x3
#a, b = [[1, 4, 6],[2, 5, -1],[3, 6, 5],[3, 6, 5]], [[4, 5, 6],[2, 2, 5],[3, 6, 5]]		

# Drittess Beispiel zum Testen: 5x4 * 4x5 = 5x5
#a, b = [[1, 4, 6, 9],[2, 5, -1, 23],[3, 6, 5, -4],[3, 6, 5, 2],[1, 4, 6, 7]], [[1, 2, 3, 3, 5],[4, 5, 6, 2, 1],[2, 2, 5, 4, -1],[3, 6, 5, -4, 2]]

# Viertes Beispiel 9x5 * 5x5 = 9x5
#a, b = [[1, 4, 6, 9, 4],[2, 5, -1, 23, 2],[3, 6, 5, -4, 2],[3, 6, 5, 2, 2],[1, 4, 6, 7, 2],[2, 5, -1, 23, 2],[2, 5, -1, 23, 2],[2, 5, -1, 23, 2],[2, 5, -1, 23, 2]], [[1, 2, 3, 3, 5],[4, 5, 6, 2, 1],[2, 2, 5, 4, -1],[3, 6, 5, -4, 2],[1, 2, 3, 3, 5]]

# Fünftes Beispiel 17x5 * 5x5 = 17x5
#a, b = [[1, 4, 6, 9, 4],[2, 2, -1, 13, 2],[2, 5, -2, 26, 5],[2, 4, -1, 24, 3],[3, 6, 0, 2, 1],[1, 5, -4, 21, 2],[2, 6, -1, 17, 3],[2, 9, -1, 22, 2],[2, 5, -1, 23, 2],[2, 5, -1, 23, 2],[3, 6, 5, -4, 2],[3, 6, 5, 2, 2],[1, 4, 6, 7, 2],[2, 5, -1, 23, 2],[2, 5, -1, 23, 2],[2, 5, -1, 23, 2],[2, 5, -1, 23, 2]], [[1, 2, 3, 3, 5],[4, 5, 6, 2, 1],[2, 2, 5, 4, -1],[3, 6, 5, -4, 2],[1, 2, 3, 3, 5]]

# Nicht Definiertes Beispiel zum Testen: 5x5 * 4x5 != 5x5
#a, b = [[1, 4, 6, 9, 4],[2, 5, -1, 23, 2],[3, 6, 5, -4, 2],[3, 6, 5, 2, 2],[1, 4, 6, 7, 2]], [[1, 2, 3, 3, 5],[4, 5, 6, 2, 1],[2, 2, 5, 4, -1],[3, 6, 5, -4, 2]]


#result = matMultDef(a,b)									#Ergebnis nach Definition ausgeben
result  = matMultSA(a,b) 									#Ergebnis nach Strassen ausgeben
															# ++ Von Hand auskommentieren je nachdem was benötigt wird ++
															
print('\n Endergebnis:\n')														
showMatrix(result)
print('\n')	
