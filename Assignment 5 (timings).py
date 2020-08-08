#Programming Assignment 5: Divide and Conquer
# Name, Vorname: Frankreiter, Florian
# Matr.-Nr: 796762

import datetime

def teile_herrsche(L,startIndex,endIndex):
    if len(L) == 0:                     # Fall Liste leer
        return False
    if len(L) == 1:                     # Fall Liste hat nur ein Element
        if L[0] == 0: return True
        else: return False
    if endIndex < startIndex or endIndex > len(L) or startIndex < 0:    # Fall Parameter 1 oder 2 invalide
        return False
    if startIndex == endIndex:          # D/C 1
        if L[startIndex] == 0:          # 0 gefunden
            return True
        else:                           # 0 nicht gefunden
            return False

    piv = (startIndex + endIndex) // 2  # Mittelpunkt berechnen

    if teile_herrsche(L,startIndex,piv) == True: return True    # Falls 0 gefunden kann abgebrochen werden
    if teile_herrsche(L,piv+1,endIndex) == True: return True    # Falls 0 gefunden kann abgebrochen werden

    return False                                                # 0 wurde nicht gefunden

def it(L):
    if 0 in L:
        return True
    else:
        return False

def brute(L):
    for i in range(len(L)):
        if L[i] == 0:
            return True
    return False

def rec(L):
    if L[0] == 0:
        return L[0]
    return rec(L[1:])


L=[i for i in range(1,11111998)]
L.append(0)

t1 = datetime.datetime.now()
print(teile_herrsche(L,0,len(L)-1))
t2 = datetime.datetime.now()
print("Teile-Herrsche: " + str(t2-t1))

#t1 = datetime.datetime.now()
#print(rec(L))
#t2 = datetime.datetime.now()
#print("Rekursiv: " + str(t2-t1))

t1 = datetime.datetime.now()
print(it(L))
t2 = datetime.datetime.now()
print("Iterativ (in): " + str(t2-t1))

t1 = datetime.datetime.now()
print(brute(L))
t2 = datetime.datetime.now()
print("Brute Force: " + str(t2-t1))
