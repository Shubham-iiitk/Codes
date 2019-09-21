class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,data):
        self.items.insert(0,data)
    def dequeue(self):
        self.items.pop()
    def peek(self):
        print(self.items[0])


q= Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
print(q.isEmpty())
q.peek()
q.dequeue()
print(q.items)
