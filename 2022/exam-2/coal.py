"""
dla kazdego transportu sprawdzamy do jakiego magazynu go nalezy włozyc i zapmiętujemy
który to był magazyn. Zwracamy indeks magazynu ostatniego transportu. O(n^2).
"""

def coal( A, T ):
    n = len(A)
    magazyny = [T for _ in range(n)]
    idx = [-1 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if magazyny[j] >= A[i]:
                magazyny[j] -= A[i]
                idx[i] = j
                break
    
    return idx[-1]