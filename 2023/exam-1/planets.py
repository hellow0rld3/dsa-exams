from math import inf

"""
f(i, j) - najtanszy koszt dostania sie na planete i, majac j litrów paliwa.

Base Case:
f(0,j) = C[0] * j

"""

def planets( D, C, T, E ):
    n = len(D)
    f = [[inf for _ in range(E+1)] for _ in range(n)]

    #Base Case
    for j in range(E+1):
        f[0][j] = C[0] * j

    #Recursion
    for i in range(n):
        for j in range(E+1):
            #teleporty
            for t in range(i):
                dest, cost = T[t]
                if dest != t and dest == i:
                    f[i][j] = min(f[i][j], f[t][0] + cost + j*C[i])

            #zwykły przelot
            for prev in range(i):
                dist = D[i] - D[prev]
                if dist <= E:
                    for diff in range(dist, E+1):
                        if diff <= E:
                            f[i][j] = min(f[i][j], f[prev][diff] + max(0, j-(diff-dist)) * C[i])
    return min(f[n-1])