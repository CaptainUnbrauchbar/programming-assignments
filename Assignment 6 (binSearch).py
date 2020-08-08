#Programming Assignment 6: Binary Search
# Name, Vorname: Frankreiter, Florian
# Matr.-Nr: 796762

def binarySearch(string,s,start,end):
    piv = (start + end) // 2
    if string[piv] == s: return True
    if ord(string[piv]) > ord(s) and piv > start:
        return binarySearch(string,s,start,end-1)
    if ord(string[piv]) < ord(s) and piv < end:
        return binarySearch(string,s,start+1,end)
    else: return False
    
	
def binSearch(string,s):
    x = sorted(string)
    string = "".join(x)
    
    if len(string) == 0: return False
    if len(string) == 1:
        if string[0] == s: return True
        else: return False
    else:
        return binarySearch(string,s,0,len(string)-1)

if __name__ == '__main__':
    string = "#3Td"
    s="s"
    print(binSearch(string,s))
    
string = "#3Td"
s="s"
print(string + " -> " + str(binSearch(string,s)) + " ('" + s + "')")

string="!)+/38?KSR"
s=")"
print(string + " -> " + str(binSearch(string,s)) + " ('" + s + "')")

string="!"
s="!"
print(string + " -> " + str(binSearch(string,s)) + " ('" + s + "')")

string="!"
s="2"
print(string + " -> " + str(binSearch(string,s)) + " ('" + s + "')")

string=""
s="!"
print(string + " -> " + str(binSearch(string,s)) + " ('" + s + "')")

string="!)+/38?KSR2 gz5,5mp2o23h5/*-+&%$§§`+###<>><<><.,.,-.,!§$%&^^°=)(//Bajk habasd h8ou84ruhakjdbjh9o"
s=">"
print(string + " -> " + str(binSearch(string,s)) + " ('" + s + "')")

string="safag3\"5"
s="\""
print(string + " -> " + str(binSearch(string,s)) + " ('" + s + "')")
