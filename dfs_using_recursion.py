
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


def dfs1(graph, node, visited):
    print(node,end='')
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            if n not in visited:
                dfs1(graph,n, visited)
    return visited
print("dfs without set() function")
dfs1(graph1,'A', [])
'''''
print()
print("dfs with set() function")
def dfs3(graph,node,visited):
    print(node,end='')
    if node not in visited:
        visited.add(node)
    for i in graph[node]:
        if i not in visited:
            visited.add(i)
            dfs3(graph,i,visited)

vis=set()
dfs3(graph1,'A',vis)

'''''




