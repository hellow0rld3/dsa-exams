"""
Jedynie sortujemy tablice i zaczynamy brać śnieg malejąco, wliczając jego topnienie.
"""

def snow( S ):
    new_tab = S
    new_tab.sort()
    new_tab.reverse()
    amount = 0
    for i in range(len(S)):
        amount += new_tab[i] - i if new_tab[i] - i > 0 else 0
    return amount