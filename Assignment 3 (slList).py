# Programming Assignment 3: Singly linked list 
# Name, Vorname: Frankreiter, Florian
# Matr.-Nr: 796762

class OperatingSystem:
    #constructor
    def __init__(self, name=None, date=None):
        self.name = name
        self.releaseDate = date
        self.next = None

class Timeline:
    #constructor creates a new empty timeline
    def __init__(self):
        self.head = None
    
    #function to traverse the elements and print out the name and the release date
    def traverse(self):
        L=[]
        actualNode = self.head
        while actualNode is not None:
            L.append((actualNode.name, actualNode.releaseDate))
            actualNode = actualNode.next
        return L

    #function inserting a new element into the timeline, overload compatibility when a already existing OperatingSystem is given
    def insert(self,name=None,releaseDate=None,os=None):
        #create a new instance of Operating System class depending on parameters given
        if os == None:
            newOS = OperatingSystem(name,releaseDate)
        else:
            newOS = os

        #set the currentNode element to head element
        currentNode = self.head
        #check if we can insert at the beginning (case 1)
        if (newOS.releaseDate <= currentNode.releaseDate):
            if newOS.releaseDate == currentNode.releaseDate:
                return "invalid year"
            newOS.next=self.head
            self.head=newOS
            return "inserted"
        #traverse list until the next nodes releaseDate is bigger than the current nodes releaseDate (case 2)
        while currentNode.next != None:
            if newOS.releaseDate <= currentNode.next.releaseDate:
                if newOS.releaseDate == currentNode.next.releaseDate:
                    return "invalid year"
                newOS.next = currentNode.next
                currentNode.next = newOS
                return "inserted"
            currentNode = currentNode.next  #traverse
        #when at the end just put it on the back of the list (case 3)
        if currentNode.next == None:
            currentNode.next = newOS
            return "inserted"
        

#Instances of Operating system class
os1=OperatingSystem("Unics",1969)
os2=OperatingSystem("Windows 95",1995)
os3=OperatingSystem("Mac OS X", 2000)

#Instance of Timeline class
timeline = Timeline()
#set os1 as the first element in timeline
timeline.head = os1
#set os2 as the second element in timeline
timeline.head.next = os2
#set os3 as the third element in timeline
os2.next = os3

print(timeline.traverse())

#this command should insert an OS into the timeline (did my own case testing)
print(timeline.insert("Testsystem 1.0",1903))
print(timeline.insert("Linux 0.1",1990))
print(timeline.insert("Red Hat Linux 6.2E",1990))
print(timeline.insert("Red Hat Linux 6.2E",2000))
print(timeline.insert("Red Hat Linux 6.5E",2005))
print(timeline.insert("Testsystem 1.1",1906))
print(timeline.insert("Red Hat Linux 6.2E",1903))
print(timeline.insert("Testsystem 0.9",1901))
print(timeline.insert("Red Hat Linux 6.2E",2000))
print(timeline.insert("Red Hat Linux 6.2E",1903))
print(timeline.insert(os=OperatingSystem("Überladungssystem",2200)))

print(timeline.traverse())