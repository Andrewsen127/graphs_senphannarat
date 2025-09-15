import sys
from .heapq import heappush, heappop   # use your own heapq implementation

def dijkstra(graph, source): 
    dist = [sys.maxsize] * len(graph)
    dist[source] = 0
    
    heap = []
    heappush(heap, (0, source))
    
    path = {source: []}  # initialize path for the source
    
    while heap:
        w, u = heappop(heap)
        
        for v in graph[u]:
            if w + graph[u][v] < dist[v]:
                dist[v] = w + graph[u][v]
                heappush(heap, (dist[v], v))
                path[v] = path[u] + [u]
    
    return dist, path
