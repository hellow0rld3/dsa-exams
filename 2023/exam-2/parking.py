from math import inf

"""
f(i,j) - najlepsze polaczenie budynkow z parkingami do i+1 indeksu, gdzie
budynek i jest połączony z budynkiem j

base case:
f(0, j) = dist(0, j)

"""

def parking(X,Y):
  m = len(X)
  n = len(Y)
  f = [[inf for _ in range(n)] for _ in range(m)] 

  #base case
  for j in range(n):
    f[0][j] = min(f[0][j-1],abs(X[0] - Y[j]))
  #recursion

  for i in range(1,m):
    for j in range(i,n):
      f[i][j] = min(f[i][j-1], f[i-1][j-1] + abs(X[i]- Y[j]))
    
  return min(f[m-1])