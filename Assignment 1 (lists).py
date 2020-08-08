# Name:         Florian Frankreiter
# MatrikelNr:   796762

import sys


def main(N):
    if (N % 2) == 0:
        isEven = True
    char = chr(N)

    listeNachfolger = []
    counter = 0
    x = N
    while True:
        x += 1
        if (x % 5) != 0:    
            listeNachfolger.append(x)
            counter += 1
        if (counter == 5):
            return [isEven,char,listeNachfolger,func(N)]
    

def func(N):
    if (N % 2) == 0:
        isEven = True
    listeZahlen = []
    if (isEven):
        for i in range(14,N,14):
            listeZahlen.append(i)
    else:  
        for i in range(17,N,17):
            listeZahlen.append(i)

    return listeZahlen

print(main(98))

