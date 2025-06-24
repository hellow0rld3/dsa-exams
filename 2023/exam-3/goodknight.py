from math import inf
from queue import PriorityQueue

"""
Zamiana postaci grafu, a potem zmodyfikowana dijkstra ktora
bierze do kolejki (dystans, wierzcholek, nieprzespane_godziny).
"""

def matrix_to_list(graph):
  n = len(graph)
  new_graph = [[] for _ in range(n)]
  for i in range(n):
    for j in range(i+1, n):
        w = graph[i][j]
        if w != -1:
           new_graph[i].append((j, w))
           new_graph[j].append((i,w))
  return new_graph


def dijkstra(graph, s, t):
   n = len(graph)
   dist = [inf] * n

   queue = PriorityQueue()
   dist[s] = 0
   queue.put((0, s, 0)) #dist, u, awake

   while not queue.empty(): 
      h, u, j = queue.get()
      for v, w in graph[u]:
        alt = dist[u] + w
        if j + w <= 16:
           if dist[v] > alt:
              dist[v] = alt
              queue.put((dist[v], v, j+w))
        else:
           if dist[v] > alt + 8:
              dist[v] = alt + 8
              queue.put((dist[v], v, 0))

   return dist[t]
      


def goodknight( G, s, t ):
  return dijkstra(matrix_to_list(G), s, t)