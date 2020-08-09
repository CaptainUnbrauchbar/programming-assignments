#Iterativ
def f(n):
    erg = 1
    for n in range(1,n+1):
        erg = n*erg
    return erg

#Rekursiv
def g(n):
    if n == 1:
        return n
    return g(n-1) * n

print("Iterativ: " + str(f(5)))
print("Rekursiv: " + str(g(5)))


