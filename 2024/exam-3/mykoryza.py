from queue import Queue
from math import inf


"""
Puszczamy algorytm BFS shortest paths z kazdego wierzchołka z źródłem grzyba, sprawdzamy jak szybko
konkretne grzyby mogą sie dostać do konkretnych wierzchołków. Jeśli jakiś grzyb moze dostać się szybciej
to nadpisujemy wartość oraz rodzaj grzyba. Jeśli mogą się dostać w tym samym czasie to następuje reguła konkurencji.
"""
      
def mykoryza( graph,T,d ):
    n = len(graph)
    queue = Queue()
    distance = [inf for _ in range(n)]
    fungi = [None for _ in range(n)]

    #dodajemy grzyby
    for i in range(len(T)):
        queue.put((T[i], i))
        distance[T[i]] = 0
        fungi[T[i]] = i

    while not queue.empty():
        u, g = queue.get()
        for v in graph[u]:
            #jesli mamy jakiego grzyba ktory przyjdzie do drzewa v szybciej
            if distance[v] > distance[u] + 1:
                distance[v] = distance[u] + 1
                fungi[v] = g
                queue.put((v, g))
            #regula konkurencji jesli grzyby sie spotakaja w tej samej turze
            if distance[v] == distance[u] + 1:
                if fungi[v] > g:
                   fungi[v] = g
                   queue.put((v, g))
    
    #liczymy ile jest drzew z grzybem d
    cnt = 0
    for grzybek in fungi:
        if grzybek == d:
            cnt += 1
    return cnt