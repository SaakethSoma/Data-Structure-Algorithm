'''
Depth First Search : (DFS)
-> searching in a deeper way
-> DFS uses stack / Recursion

Approach : 1) start with main node
           2) go to one neighbour
           3) Keep going deeper
           4) Back track when struck


'''
def dfs(graph,node,visited):
    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)

graph = {
    'A' : ['B','C'],
    'B' : ['D'],
    'C' : ['D'],
    'D' : []
}
visited = set()
dfs(graph,'A',visited)