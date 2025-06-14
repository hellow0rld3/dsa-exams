from math import inf

"""
f(i, j) = najwieksza suma podciagu konczacego sie na i przy j usuniętych elementach
               f(i-1, j-1)                , usuwamy i-ty element, dodajemy jedno ciecie
f(i, j) = max{ f(i-1, j) + T[i] }         , dodajemy i-ty element
               T[i]                       , rozpoczynamy nowy podciag

Base case: f(i, i) = 0
"""
def kstrong(T, k):
   n= len(T)

   if k > n:
      k = n

   #tablica memo
   f = [[0 for _ in range(k+1)] for _ in range(n+1)]

   #Base Cases
   for l in range(min(n+1,k+1)):
      if l <= k:
        f[l][l] = 0 
  
   for m in range(1,k+1):
      f[0][m] = -inf

   #Rekurencja
   maksimum = -inf
   for i in range(1, n+1):
      for j in range(k+1):
         f[i][j] = max(T[i-1], f[i-1][j] + T[i-1])
         if j >= 1:
            f[i][j] = max(f[i][j], f[i-1][j-1])
         maksimum = max(maksimum, f[i][j])

   return maksimum

