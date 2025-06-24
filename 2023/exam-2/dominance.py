from math import inf

def dominance(P):
  n = len(P)

  x = [0] * (n + 1)
  y = [0] * (n + 1)

  for point in P:
    x[point[0]] += 1
    y[point[1]] += 1

  for i in range(n - 1, -1, -1):
    x[i] += x[i + 1]
    y[i] += y[i + 1]
  minimum = inf

  for point in P:
    not_dominated = x[point[0]] + y[point[1]]
    minimum = min(minimum, not_dominated)
 
  return n - (minimum - 1)