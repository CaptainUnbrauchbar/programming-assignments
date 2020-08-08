#Programming Assignment 7: Insertion sort
# Name, Vorname: Frankreiter, Florian
# Matr.-Nr: 796762

languages={"Javascript": 1, "Java": 2, "Python": 3, "CSS": 4, "PHP": 5, "Ruby": 6, "C++": 7, "C": 8, "Shell": 9, "C#": 10}

def insertionSort(L):
    if len(L) == 0 or len(L) == 1:      #liste ist leer oder hat nur ein Element
        return L
    for i in range(1, len(L)):
        temp = L[i]
        j = i-1
        if temp not in languages or L[j] not in languages:      #programmiersprache nicht definiert
            return L
        while j >= 0 and languages[temp] > languages[L[j]]:     #sortieren mit tausch anstatt mit neuer liste, sodass in place
            L[j+1] = L[j]
            j -= 1
        L[j+1] = temp
    return L


# code to test your implementation

if __name__ == '__main__':
    L = ['Java','Shell','CSS']
    print(insertionSort(L))
    L = ['Java','Shell','CSS','Java','Shell','CSS','Java','Shell','CSS','Java','Shell','CSS','Java','Shell','CSS','C++','Python','Javascript','Ruby','PHP']
    print(insertionSort(L))
    L = ['C++','Python','Javascript','Ruby','PHP']
    print(insertionSort(L))
    L = ['CSS','C#','C#','C++','Ruby']
    print(insertionSort(L))
    L = ['Ruby','Python','Java','Java']
    print(insertionSort(L))
    L = ['Ruby']
    print(insertionSort(L))
    L = [""]
    print(insertionSort(L))
    L = [[]]
    print(insertionSort(L))
    
    # Tests mit nicht definierten Sprachen
    L = ['SQF']
    print(insertionSort(L))
    L = ['SQF','Java', 'PHP']
    print(insertionSort(L))
    L = ['Java', 'SQF', 'PHP']
    print(insertionSort(L))
    L = ['SQF', 'SQF', 'SQF', 'SQF']
    print(insertionSort(L))