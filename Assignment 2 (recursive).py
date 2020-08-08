#Programming Assignment 2: Recursion 
# Name, Vorname: Frankreiter, Florian
# Matr.-Nr: 796762



def string_reverse(s):
    if len(s) == 0:
        return s
    else:
        return string_reverse(s[1:]) + s[0]

s = '1234'
print(string_reverse(s))
