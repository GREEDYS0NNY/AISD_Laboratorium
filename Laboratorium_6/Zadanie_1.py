tab = [1, 2, 10, 11, 12, -5, -8, 10, 11]
x = int(input('Poszukiwany element: '))
count = 0

for i in range(len(tab)):
    if tab[i] == x:
        count += 1
        print(f'Element "{tab[i]}" występuje w zbiorze.')
if count == 0:
    print('Poszukiwanego elementu w zbiorze nie ma.')
