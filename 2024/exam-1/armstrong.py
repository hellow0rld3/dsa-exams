from queue import PriorityQueue
from math import inf, floor

def build_graph(edges):
  n = max(map(lambda x: max(x[0], x[1]), edges)) + 1
  graph = [[] for _ in range(n)]

  for u,v,w in edges:
    graph[u].append((v,w))
    graph[v].append((u,w))

  return graph

def dijkstra(graph, s):
  n = len(graph)

  distance = [inf] * n
  Q = PriorityQueue()

  distance[s] = 0
  Q.put((0, s))

  while not Q.empty():
    d, u = Q.get()

    if d > distance[u]:
      continue

    for v, w in graph[u]:
      relax = distance[u] + w
      if distance[v] > relax:
        distance[v] = relax
        Q.put((relax, v))
  return distance



def armstrong( B, G, s, t):
  graph = build_graph(G)

  distances_s = dijkstra(graph, s)
  distances_t = dijkstra(graph, t)

  result = distances_s[t]

  for u,p,q in B:
    result = min(result, distances_s[u] + distances_t[u] * (p/q))

  return floor(result)

