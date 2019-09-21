# Adjecent Matrix for undirected graph

class AdjMatrix:

    def __init__(self,size):
        self.size=size
        self.matrix=[]
        for i in range(size):
            self.matrix.append([0 for j in range(size)])

    def addedge(self, v1,v2):
        if v1==v2:
            return
        else:
            self.matrix[v1][v2]=1
            self.matrix[v2][v1]=1

    def printAdjMatrix(self):
        print(self.matrix)

    def remove(self,v1,v2):
        if self.matrix[v1][v2]==0:
            print("No edge is present")
        else:
            self.matrix[v1][v2] =0
            self.matrix[v2][v1] =0


a =AdjMatrix(int(input("enter the size of adjecent matrix ")))
n = int(input("enter the number of edges "))
for i in range(n):
    u, v = [int(x) for x in input("Enter two value: ").split()]
    a.addedge(u,v)
a.printAdjMatrix()

#a =AdjMatrix(4)
# a.addedge(1,1)
# a.addedge(1,2)
# a.addedge(2,1)
# a.addedge(3,1)
# a.addedge(3,2)
# a.printAdjMatrix()
# a.remove(3,2)
# a.printAdjMatrix()


