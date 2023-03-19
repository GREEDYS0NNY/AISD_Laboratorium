"""
Algorytm, który znajduje wartość minimalną w tablicy dwuwymiarowej w każdym wierszu.
Po znalezieniu minimalnej wartości jest ona wstawiana na początek danego wiersza.
"""

tab = [[14, 10, 11], [20, 21, 9], [5, 4, 13]]
for wiersz in range(len(tab)):
    min_wartość = tab[wiersz][0]
    min_index = 0
    for wartość_wiersza in range(1, len(tab[wiersz])):
        if tab[wiersz][wartość_wiersza] < min_wartość:
            min_wartość = tab[wiersz][wartość_wiersza]
            min_index = wartość_wiersza
    if min_index != 0:
        del tab[wiersz][min_index]
        tab[wiersz].insert(0, min_wartość)
print(tab)
