def wieża_hanoi(n, aktualny, roboczy, docelowy):
    if n == 1:
        print(f'Przenosimy krążek {n} z patyka {aktualny} na patyk {docelowy}.')
    else:
        wieża_hanoi(n - 1, aktualny, docelowy, roboczy)
        print(f'Przenosimy krążek {n} z patyka {aktualny} na patyk {docelowy}.')
        wieża_hanoi(n - 1, roboczy, aktualny, docelowy)


wieża_hanoi(5, "A", "B", "C")
