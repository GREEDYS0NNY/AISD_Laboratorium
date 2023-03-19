"""
Algorytm wyszukiwania w tablicy jednowymiarowej minimalnej wartości.
"""

tab = [10, 4, 5, 2, 3, 9, 11, 20, 1]
min_wartość = tab[0]

for i in range(1, len(tab)):
    if tab[i] < min_wartość:
        min_wartość = tab[i]
print(min_wartość)
