graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

def bfs(graph,node):
    visited=set()
    stack=[node]
    while stack:
        v=stack.pop(0)
        if v not in visited:
            visited.add(v)
            print(v,end='')
            for i in graph[v]:
               if i not in visited:
                 stack.append(i)
print("bfs of given graph:")
bfs(graph1,'A')
print()

def dfs(graph,node):
    visited = set()
    stack =[node]
    while stack:
        v= stack.pop()
        if v not in visited:
            visited.add(v)
            print(v,end='')
            for n in graph[v]:
                stack.append(n)



print("dfs of given graph")
dfs(graph1,'A')