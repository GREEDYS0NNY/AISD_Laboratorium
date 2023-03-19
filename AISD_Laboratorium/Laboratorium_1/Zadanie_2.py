"""
Algorytm wczytywania ciągu n liczb całkowitych (N>0) i wyznaczania ilości liczb
ujemnych w tym ciągu.
"""

n = int(input('Podaj ilośc elementów: '))
ilość_u = 0

for l in range(n):
    liczba = int(input('Podaj liczbę: '))
    if liczba < 0:
        ilość_u += 1
print(f'Ilość liczb ujemnych = {ilość_u}')
