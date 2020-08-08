#Programming Assignment 10: Search Tree 
# Name, Vorname: Frankreiter, Florian
# Matr.-Nr: 796762


class OperatingSystem:
    #constructor
    def __init__(self, name=None, date=None):
        self.name = name
        self.releaseDate = date
        self.left = None
        self.right = None

    #destructor
    def __del__(self):
        return 0

    #traverse the tree in preorder and save the nodes in the list
    def traverseAndPrint(self,L=[]): 
        L.append((self.name, self.releaseDate))
        if self.left:
            self.left.traverseAndPrint(L) 
        
        if self.right:
            self.right.traverseAndPrint(L) 
        return L
            
    #simplified add method which assumes that the nodes are coming in the correct sequence
    def add(self, os):
        if os.releaseDate < self.releaseDate:
            if self.left:
                return self.left.add(os)
            else:
                self.left = os
        else:
            if self.right:
                return self.right.add(os)
            else:
                self.right = os

    #it is assumed that the root is never removed
    def remove(self, releaseDate):
        parent = None
        node = self

        #Find Node and save parent
        while node != None and node.releaseDate != releaseDate:
            parent = node
            if releaseDate < node.releaseDate:
                node = node.left
            else:
                node = node.right

        #Case Node has no Children
        if node.left == None and node.right == None:
            if parent.right == node:
                parent.right = None
            if parent.left == node:
                parent.left = None
            return "removed"

        #Case node only has right child
        if node.left == None:
            if parent.right == node:
                parent.right = node.right
            if parent.left == node:
                parent.left = node.right
            return "removed"
        
        #Case node only has left child
        if node.right == None:
            if parent.right == node:
                parent.right = node.left
            if parent.left == node:
                parent.left = node.left
            return "removed"

        #Case node has 2 childs
        else: 
            mrol = node.left
            mrolparent = None
            while mrol.right != None:
                mrolparent = mrol
                mrol = mrol.right

            if parent.right == node:
                parent.right = mrol
                if mrolparent != None:
                    mrolparent.right = mrol.left
                    mrol.left = node.left           
                mrol.right = node.right
                
            if parent.left == node:
                parent.left = mrol
                if mrolparent != None:
                    mrolparent.right = mrol.left
                    mrol.left = node.left
                mrol.right = node.right
            return "removed"



     
os1 = OperatingSystem("Debian 1.1",1996)
os2 = OperatingSystem("1BSD",1977)
os1.add(os2)
os3 = OperatingSystem("Windows 10",2015)
os1.add(os3)
os4 = OperatingSystem("Unics",1969)
os1.add(os4)
os5 = OperatingSystem("Mac OS X", 2000)
os1.add(os5)
os6=OperatingSystem("Windows 95",1995)
os1.add(os6)
os7 = OperatingSystem("macOS Catalina",2019)
os1.add(os7)

if __name__ == '__main__':
    print(os1.traverseAndPrint(L=[]))
    print(os1.remove(2015))
    print(os1.traverseAndPrint(L=[]))
    print(os1.remove(1977))
    print(os1.traverseAndPrint(L=[]))
    print(os1.remove(2019))
    print(os1.traverseAndPrint(L=[]))
    print(os1.remove(1969))
    print(os1.traverseAndPrint(L=[]))
    print(os1.remove(1995))
    print(os1.traverseAndPrint(L=[]))
    print(os1.remove(2000))
    print(os1.traverseAndPrint(L=[]))