def S(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n > 1:
        s = [1, 1]

        for i in range(2, n + 1):
            s.append(2 * s[i - 1] - s[i - 2])
        print(s)
        return s[n]


n = int(input('Podaj n: '))
if n > 0:
    print(S(n))
else:
    print('Podano zle dane')
