#Programming Assignment 9: Hashing
# Name, Vorname: Frankreiter, Florian
# Matr.-Nr: 796762

def hashing(L):
    hashTabelle={0:'leer',1:'leer',2:'leer',3:'leer',4:'leer',5:'leer',6:'leer',7:'leer',8:'leer',9:'leer',10:'leer'}
    if len(L) == 0:
        return hashTabelle
    for i in range(0,len(L)):
        h = L[i] % 9                                # hashfunktion h_i = n mod 9
        if hashTabelle[h] == 'leer':                # basisfall, kein sondieren nötig
            hashTabelle[h] = L[i]
        else:                                       # lineares sondieren, max Schrittweite 11
            for j in range(len(hashTabelle)):
                k = h+j
                if k > 10: k -= 11                  # Nach Index 10 bei 0 weitermachen
                if hashTabelle[k] == 'leer':
                    hashTabelle[k] = L[i]
                    break
    
    return hashTabelle


 #code to test your implementation
if __name__ == '__main__':
    L=[4,78,45,12,3]
    print(hashing(L))
    L=[90,2,67,1089,54,34,78,21,156,1000,19]
    print(hashing(L))
    L=[90,90,90,90,90,93,90,90,90,90,90]
    print(hashing(L))
    L=[]
    print(hashing(L))
    L=[1,2,3,4,5,6,7,8,9,10,11,12]
    print(hashing(L))

