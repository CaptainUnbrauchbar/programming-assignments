#Programming Assignment 4: Matrix Multiplication 
# Name, Vorname: Frankreiter, Florian
# Matr.-Nr: 796762

def matrixMult(M1,M2):
    if len(M1[0]) != len(M2):       # Fehlerbehandlung (m x (n = m) x n)
        return 'invalid input'
    else:
        M3 = []
        for i in range(len(M1)):
            M3.append([])                                   # Leere Spalte einfügen
            for j in range(len(M2[0])):
                M3[i].append(0)                             # Leere Zeile einfügen
                for k in range(len(M2)):
                    M3[i][j] += M1[i][k] * M2[k][j]	        # Wert einfügen
        return M3

M1 = [[2]]
M2 = [[5]]

print(matrixMult(M1,M2))