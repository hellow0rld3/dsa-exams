from math import inf

"""
Dla kazdego podciagu (i,j) sortujemy go i usuwamy elementy dopóki są ujemne lub dopóki usunęliśmy ich maksymalnie k
dla kazdej iteracji zapisujemy sume i porównujemy z maksymalna suma do tej pory. Rozwiazanie ma zlozonosc:
n^2 * nlogn * k = O(n^2logn) [zlozonosc akceptowalna, nie potrafie rozwiazac na zlozonosc O(nk)] Rozwiazanie suboptymalne,
"""

def kstrong( T, k):
  if not T:
     return 0
    
  n = len(T)
  max_sum = float('-inf')
    
  for i in range(n):
    for j in range(i, n):
        subarray = sorted(T[i:j+1])
            
        current_sum = sum(subarray)
        best_sum = current_sum
            
        for remove_count in range(1, min(k + 1, len(subarray) + 1)):
            current_sum -= subarray[remove_count - 1]
            best_sum = max(best_sum, current_sum)
            
        max_sum = max(max_sum, best_sum)
    
  return max_sum

