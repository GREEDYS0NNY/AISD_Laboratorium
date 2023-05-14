from collections import deque


def gra_goracego_ziemniaka(uczestnicy, liczba_operacji):
    kolejka = deque(uczestnicy)

    while len(kolejka) > 1:
        for _ in range(liczba_operacji - 1):
            kolejka.append(kolejka.popleft())

        eliminowany_uczestnik = kolejka.popleft()
        print(f"Eliminowany uczestnik: {eliminowany_uczestnik}")

    zwyciezca = kolejka.popleft()
    print(f"Zwycięzca: {zwyciezca}")


uczestnicy = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
liczba_operacji = 3

gra_goracego_ziemniaka(uczestnicy, liczba_operacji)
