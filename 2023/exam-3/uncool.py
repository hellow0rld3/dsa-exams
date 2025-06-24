"""
Tworzymy listę z indeksami i sortujemy według początku przedziału, przechodzimy przez posortowane przedziały, dla których sprawdzamy przedziały które zaczynają się później. Jeśli mamy przecięcie,
to sprawdzamy czy para jest niefajna - sprawdzamy czy jedenzawiera się w drugim i jeśli nie,
to mamy parę niefajną.
"""

def uncool( P ):
  n = len(P)

  intervals_with_idx = [(P[i][0], P[i][1], i) for i in range(n)]
  intervals_with_idx.sort()
    
  for i in range(n):
    start_i, end_i, idx_i = intervals_with_idx[i]
        
    for j in range(i + 1, n):
      start_j, end_j, idx_j = intervals_with_idx[j]

      #Jeśli start_j > end_i, to wszystkie kolejne przedziały będą rozłączne więc mozemy przerwać 
      if start_j > end_i:
        break
                
            
      first_contains_second = (start_i <= start_j and end_j <= end_i)
      second_contains_first = (start_j <= start_i and end_i <= end_j)
            
      if not first_contains_second and not second_contains_first:
        return (idx_i, idx_j)