from math import inf 

"""
f(i, j) = najdluzsza sciezka konczaca sie w indeksie i+1, z j k-pechowymi liczbami

if i = kpechowa and j > 0:
    f(i, j) = max{f(i-1, j-1) + 1, 0}
else if i != kpechowa:
    f(i, j) = f(i-1, j) + 1
"""




def kunlucky(T, k):
    n= len(T)

    def unlucky_arr(k, lim):
        arr = [k]
        num = k
        i = 1
        while num < lim:
            num = num + (num%i) + 7
            i += 1
            arr.append(num)
        return arr[:-1]
    
    unlucky = unlucky_arr(k, n+1)
    boolean = [False for _ in range(n+1)]
    for element in unlucky:
        boolean[element] = True 

    
    f = [[-inf for _ in range(3)] for _ in range(n + 1)]
    for i in range(n+1):
        f[i][0] = 0

    for i in range(1, n+1):
        for j in range(3):
            if boolean[T[i-1]] is True and j > 0:
                f[i][j] = max(f[i-1][j-1] + 1, 0)
            if boolean[T[i-1]] is False:
                f[i][j] = f[i-1][j] + 1

    maksimum = -inf
    for i in range(n+1):
        for j in range(3):
            maksimum = max(maksimum, f[i][j])
    return maksimum
