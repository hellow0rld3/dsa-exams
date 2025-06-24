"""
F[i] - maksymalna ilosc złota przy wejściu do i-tej komnaty

Base Case:
F[0] = 0

Rekruencja:
F[i] = max(F[i], F[t] + gold_t), gdzie t to kazda komnata prowadzaca do i.

Dla kazdej komnaty i, patrzymy w przod na komnaty do ktorych mozemy dotrzec i to dla nich
przypisujemy wartości w tablicy memo. Jeśli przechodzimy przez komnate do której i tak nie da
się dotrzeć to nalezy pominac proces. Na koniec zwracamy wartość tablicy memo dla ostatniej komnaty.

"""

def magic( C ):
    n = len(C)
    F = [-1] * n 
    F[0] = 0

    for i in range(n):
        if F[i] == -1:
            continue

        g = C[i][0]

        take = min(g,10)
        g -= take

        caves = C[i][1:]
        
        for price, dest in caves:
            if dest == -1 or price < g:
                continue

            payment = price - g
            F[dest] = max(F[dest], F[i] + take - payment)

    return F[n-1]