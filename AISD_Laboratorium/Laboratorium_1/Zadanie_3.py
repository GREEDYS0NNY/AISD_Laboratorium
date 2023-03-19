"""
Algorytm, który sprawdza czy podana przez użytkownika wartość
występuje w tablicy jednowymiarowej.
"""

tab_j = [1, 2, 3, 4, 5, 6]
występuje = False

wartość = int(input('Wartość do wyszukania: '))

for i in tab_j:
    if i == wartość:
        występuje = True
        break

if występuje == True:
    print('Wartość występuje w tablice')
else:
    print('Wartość nie występuje w tablicy')
