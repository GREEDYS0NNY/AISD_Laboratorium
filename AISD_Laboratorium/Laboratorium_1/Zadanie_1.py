"""
Algorytm wyznaczania pierwiastków równania kwadratowego.
"""

a = int(input('Liczba a: '))
b = int(input('Liczba b: '))
c = int(input('Liczba c: '))

if a != 0:
    delta = b * b - 4 * a * c
    if delta > 0:
        sqrt = delta ** 0.5
        x1 = (-b - sqrt / (2 * a))
        x2 = (-b + sqrt / (2 * a))
        print(f'x1 = {x1}, x2 = {x2}')
    elif delta == 0:
        x = -b / (2 * a)
        print(f'x = {x}')
    else:
        print('Brak rozwiązań rzeczywistych')
else:
    print('To nie jest równanie kwadratowe')
