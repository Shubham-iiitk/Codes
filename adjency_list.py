from collections import defaultdict

# Adjlist without using class


m = defaultdict(list)
def adjlist(v1,v2):  
    if v1!=v2:
       if v1 not in m:
         m[v1]=[v2]
       else:
          m[v1].append(v2)

adjlist(1,2)
adjlist(1,3)
adjlist(2,1)
adjlist(1,3)
adjlist(2,3)
print(m,'hfuas')



# dictionary using class
'''''
class Graph:
    def __init__(self,directed=False):
        self.graph=defaultdict(list)
        self.directed=directed

    def add_edge(self,u,v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def find_edge(self,u,v):
        if v in self.graph[u]:
            print("these two have adge in common")

    def remove_edge(self,u,v):
        if v in self.graph[u]:
                    self.graph[u].remove(v)


    #def dfs(self,graph,node):


g=Graph()
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(1,3)
g.add_edge(3,5)
g.add_edge(4,5)

#print(g.graph)
#g.find_edge(3,5)
#g.remove_edge(3,5)
print(g.graph)

'''''

