from math import inf
from queue import PriorityQueue

"""
Dorysowujemy alternatywny graf, który odpowiada sytuacji obrabowania zamku - przejście na niego kosztuje ujemną ilość
bo dostajemy złoto; jest jednostronne, bo nie mozna wrócić, i krawędzie w nim kosztują odpowiednio więcej, co odpowiada
sytuacji w której jesteśmy ścigani. Na tym grafie odpalamy zwykły algorytm dijkstry i zwracamy distances[t+n], bo zawsze 
na końcu chcemy obrabować ostatni zamek i wziąć dodatkowe złoto.
"""

def duplicate_graph(graph, r, V):
    n = len(graph)
    new_graph = [[] for _ in range(2*n)]

    for u in range(n):
        for v, cost in graph[u]:
            new_graph[u].append((v, cost))

    for u in range(n):
        for v, cost in graph[u]:
            new_graph[u+n].append((v+n, 2*cost + r))
    for u in range(n):
        new_graph[u].append((u+n, (-1)*V[u]))
    return new_graph
    

def dijkstra(graph, s):
    n = len(graph)
    dist = [inf] * n
    queue = PriorityQueue()

    dist[s] = 0
    queue.put((0,s))

    while not queue.empty():
        d, u = queue.get()

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                queue.put((alt, v))

    return dist

def gold(G,V,s,t,r):
    n = len(G)
    graph = duplicate_graph(G, r ,V)
    distances = dijkstra(graph, s)
    return distances[t+n]