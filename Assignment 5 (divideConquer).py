#Programming Assignment 5: Divide and Conquer
# Name, Vorname: Frankreiter, Florian
# Matr.-Nr: 796762

def teile_herrsche(L,startIndex,endIndex):
    if len(L) == 0:                     # Fall Liste leer
        return False
    if len(L) == 1:                     # Fall Liste hat nur ein Element
        if L[0] == 0: return True
        else: return False
    if endIndex < startIndex or endIndex > len(L) or startIndex < 0:    # Fall Parameter 1 oder 2 invalide
        return False
    if startIndex == endIndex:          # teile herrsche len(L) == 1
        if L[startIndex] == 0:          # 0 gefunden
            return True
        else:                           # 0 nicht gefunden
            return False

    piv = (startIndex + endIndex) // 2  # Mittelpunkt berechnen

    if teile_herrsche(L,startIndex,piv) == True: return True    # Falls 0 gefunden kann abgebrochen werden
    if teile_herrsche(L,piv+1,endIndex) == True: return True    # Falls 0 gefunden kann abgebrochen werden

    return False                                                # 0 wurde nicht gefunden



L=[1,2,3,4]
print(str(L) + " -> " + str(teile_herrsche(L,0,len(L)-1)))
L=[1,2,3,4,5]
print(str(L) + " -> " + str(teile_herrsche(L,0,len(L)-1)))
L=[8,0,6,7,11]
print(str(L) + " -> " + str(teile_herrsche(L,0,len(L)-1)))
L=[2]
print(str(L) + " -> " + str(teile_herrsche(L,0,len(L)-1)))
L=[]
print(str(L) + " -> " + str(teile_herrsche(L,0,len(L)-1)))
L=[0]
print(str(L) + " -> " + str(teile_herrsche(L,0,len(L)-1)))
L=[8,0,6,7,11,8,0]
print(str(L) + " -> " + str(teile_herrsche(L,0,len(L)-1)))
L=[0,0,0]
print(str(L) + " -> " + str(teile_herrsche(L,0,len(L)-1)))
L=[i for i in range(1,50)]
print(str(L) + " -> " + str(teile_herrsche(L,0,len(L)-1)))
L=[i for i in range(1,50)]
L.append(0)
print(str(L) + " -> " + str(teile_herrsche(L,0,len(L)-1)))

L=[8,0,6,7,11]
print(str(L) + " (1-4)" + " -> " + str(teile_herrsche(L,1,4)))

L=[8,0,6,7,11]
print(str(L) + " (2-4)" + " -> " + str(teile_herrsche(L,2,4)))
