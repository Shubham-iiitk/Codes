import collections

def bfs(graph,root ):
    visited , queue = set(), collections.deque([root])
    visited.add(root)
    print(root,end="")
    while queue:
        v = queue.popleft()
        for n in graph[v]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
                print(n,end="")

graph = {'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']}
bfs(graph,'A')