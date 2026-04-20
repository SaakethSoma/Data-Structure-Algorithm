'''
Graphs: Graph is a non-linear data structure used to create relationships.
It contains: 1) vertices(Nodes) -> points A,B,C....
             2) Edges -> connection between vertices
example : cities and its routes.

real life analogy : -> google maps , places will be nodes and route is an edge

types of graphs :
1) Unweighted Graphs: we dont have any weight for edge(distance/value)
    -> it just checks to verify the connectivity of other vertices.
    -> It is used when all the connections are equal
    -> only need connectivity

2) Weighted Graphs: we will have weight for each edge(cost/distance/time)
    -> used when distance matters(maps,networks)
    -> cost/time optimization

3) Graph representation:
 a) Adjacency list : stores neighbors of each node
    graph : { 
            a : {b,c}
            b: {a,d}
            c: {a,d}
            d: {b,c}
    }
 b) Adjacency matrix : 
    graph : [0 1 1 0] #A
            [1 0 0 1] #B
            [1 0 0 1] #C
            [0 1 1 0] #D 
            easy to understand and uses more memory
c) Graph Traversal : 
    traversal -> visiting all the nodes
Two main methods : 1) Breadth First Search(BFS): visiting nodes level by level
                    -> uses Queue(FIFO)
        real life analogy: -> Exploring the neighbours first
BFS APPROACH : 1) start from a node 
               2) visit all the neighbours
               3) then neighbours of neighbours

'''

from collections import deque
graph = {
    'A': [('B',5),('C',2)],
    'B': [('D',3)],
    'C': [('D',4)],
    'D': []
}
print("Weighted Graph:")
for node in graph:
    print(node,"->",graph[node])

def bfs_weighted(graph,start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node,end = " ")

        for neighbour,weight in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
print("\n BFS on weighted graph:")

bfs_weighted(graph,'A')

#dry run: 