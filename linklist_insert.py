class Node:
    def __init__(self,data):
        self.value= data
        self.next= None
class Linklist:
    def __init__(self):
        self.head =None

# for printing the linklist

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp= temp.next

# adding node at begning

    def addbeg(self,data):
        new = Node(data)
        new.next = l.head
        l.head = new

# adding node at end

    def addend(self,data):
        new = Node(data)
        new.next=None
        last = self.head
        while last.next:
            last =last.next
        last.next= new

# Inserting a node after a given node:

    def add(self,data,prev):
        new = Node(data)
        temp = self.head
        while temp.value != prev:
            temp =temp.next
        new.next = temp.next
        temp.next  = new



l=Linklist()
l.head= Node(1)
l2 = Node(2)
l.head.next=l2
l3=Node(3)
l2.next=l3
l.printlist()
#l.addbeg(4)
l.addend(4)
l.add(5,3)
l.printlist()
