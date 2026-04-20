'''
Graph Dijkstra Implementation on Shortest Path :
Dijkstra -> shortest path
-> It stores the problem like:
    -> Minimum Travel Time
    -> Cheapest Flight cost
    -> network routing

KEY IDEA : Always expand the node with smallest known distance

1) Dijkstra works on:
    -> Weighted Graph
    -> Directed / UnDirected Graph

2) Core Concept(Greedy Approach):
At Every Step:
    -> pick the node with minimum distance
    -> update(relax) its neighbours
    -> repeat until all nodes are visited

 3) Important terms:
    -> Distance array(dist[]) -> stores shortest distance from source
    -> Priority Queue(min heap) -> picks the minimum distance node

 Relaxation: if dist[u] + weight < dist[v]; update dist[v]

 4) step by step approach :
    a) Initialize: 
        dist[source]=0
        dist[others]=infinity
    b) Use a Min heap(priority queue)
    c) while heap not empty:
        ->extract min node v
        -> For each neighbour v:
            if shortest path found -> update
'''

import heapq

def dijkstra(graph,source):
    #initialise the distances
    dist = {node:float('inf')for node in graph}
    dist[source]=0

    #Min Heap(distance,node)
    pq = [(0,source)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        #skip if already found better path
        if current_dist > dist[current_node]:
            continue

        #explore neighbours
        for neighbour,weight in graph[current_node]:
            distance = current_dist + weight

            #relaxation
            if distance < dist[neighbour]:
                dist[neighbour]=distance
                heapq.heappush(pq,(distance,neighbour))
    return dist

#example graph(adjacency list)
graph = {
    'A':[('B',1),('C',4)],
    'B':[('C',2),('D',5)],
    'C':[('D',1)],
    'D':[]
}
result = dijkstra(graph,'A')
print(result)
