from math import inf

"""
f(i, j) = min koszt kabli na gniazdkach od i do j+1.
Ponadto, w tym przedziale szukamy takiego k, ze k-te gniazdko łączymy z i-tym gniazdkiem i dodajemy koszt ich kabla,
potem dodajemy koszt kabli dla gniazdek od i+1 do k oraz koszt pozostały koszt przedziału od k+1 do j+1.

f(i, j) = min{ 1 + abs(T[i] - T[k]) + f(i+1, k-1) + f(k+1, j) for k in range(i+1, j+1)) }

"""

def wired( T ):
    n = len(T)
    #tablica memo
    dp = [[inf for _ in range(n)] for _ in range(n)]

    for s in range(2, n+1, 2):
        for i in range(0, n-s+1):
            j = i + s -1

            for k in range(i+1, j+1, 2):
                dp[i][j] = min(dp[i][j], 1 + abs(T[i] - T[k]) + (dp[i+1][k-1] if i+1 < k-1 else 0) + (dp[k+1][j] if k+1 < j else 0) )
                               
    return dp[0][n-1] #xd