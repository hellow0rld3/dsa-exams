"""
Tworzę tablicę events, do której po kolei osobno dodaje kazde miejsce w którym śnieg zaczął lub przestał padać.
Przechowuję jako parę (lokalizacja, +/- 1), gdzie +1 oznacza ze zaczęło padać a -1, ze przestało.
sortuję tablicę po lokalizacji, czyli po pierwszej współrzędnej i szukam w niej ile razy "zaczęło padać z rzędu".
"""

def snow( T, I ):
    events = []

    for a, b in I:
        events.append((a,1))
        events.append((b+1, -1))

    events.sort(key=lambda x: (x[0], x[1]))

    max_depth = 0
    current_depth = 0

    for position, delta in events:
        current_depth += delta
        max_depth = max(max_depth, current_depth)

    return max_depth