from time import time  # wird gebraucht für Zeitmessung

# Die Routine, wie laut Übung gefordert
def teile_herrsche(L,startIndex,endIndex):
    if (endIndex <= startIndex):
        return L[startIndex] == 0
    delta = int((endIndex-startIndex)/2)
    if teile_herrsche(L,startIndex,startIndex+delta):
        return True
    return teile_herrsche(L,startIndex+delta+1,endIndex)

# Die achtfach schnellere Routine ohne Rekursion
def herrsche(L,startIndex,endIndex):
    for i in range(startIndex,endIndex+1):
        if L[i]==0:
            return True
    return False

# Länge der Liste und Zahl der Durchläufe
nmax=100000

# Ergebnisse (Laufzeiten und Histogramme) vorbereiten
tmxR=0
tmxNR=0
histR=[]
histNR=[]
for i in range(1000):
    histR.append(0)
    histNR.append(0)

# Liste initialisieren mit lauter Einsen
L=[]
for i in range(nmax):
    L.append(1)

# Gesamtlaufzeit rekursiv
start=time()
for i in range(nmax):
    L[i]=0  # immer ein Element Null setzen
    t0=time()
    teile_herrsche(L,0,nmax-1)
    dt=time()-t0   # Laufzeit des Einzelfalls
    try:   # nur zur Sicherheit, damit eine lange Laufzeit nicht zu einem Indexfehler führt
        histR[int(dt*20000.)]+=1
    except:
        pass
    if (dt>tmxR):
        tmxR = dt  # Maximale Laufzeit protokollieren
    L[i]=1  # Nullsetzung rückgängig machen

inter=time()  # Zwischenzeit nehmen
for i in range(nmax):
    L[i]=0
    t0=time()
    herrsche(L,0,nmax-1)   # hier "herrsche" statt "teile"
    dt=time()-t0
    try:
        histNR[int(dt*20000.)]+=1
    except:
        pass
    if (dt>tmxNR):
        tmxNR = dt
    L[i]=1

end=time()   # Stoppuhr anhalten

print("rekursiv: %s %s    nichtrek: %s  %s" % (inter-start, tmxR, end-inter, tmxNR))

# Histogramm abspeichern
f=open("histogramme.csv", "w")
for i in range(len(histR)):
    f.write("%s %s %s\n" % (i/20000, histR[i], histNR[i]))
f.close()


# Laufzeit-Ergebnisse mit nominell 4.2GHz (eigentlich 4-Kern+HT, ist hier aber nur single-thread)
# Ergebnis fÜr 100000 mit LL.copy(): 1382.0236368179321 180.64929056167603
# Ergebnis fÜr 100000 mit L[i]:      1378.1265223026276 152.92610573768616
# Ergebnis inc. Histogramm: rekursiv: 1347.010239124298 0.03761792182922363    nichtrek: 153.0231363773346  0.006702899932861328
