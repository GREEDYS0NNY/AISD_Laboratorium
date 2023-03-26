def sortowanie(liczby):
    n = len(liczby)
    for i in range(n):
        for k in range(i + 1, n):
            if str(liczby[i]) > str(liczby[k]):
                liczby[i], liczby[k] = liczby[k], liczby[i]
    return liczby


print(sortowanie([1, 2, 3, 11, 21, 111, 231]))
