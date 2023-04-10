def funkcja2():
    P = [[0 for i in range(6)] for j in range(6)]

    for i in range(1, 6):
        P[i][0] = 0
    for j in range(1, 6):
        P[0][j] = 1
    for i in range(1, 6):
        for j in range(1, 6):
            P[i][j] = round((P[i - 1][j] + P[i][j - 1]) / 2, 2)
    for row in P:
        print(row)
    return f'Wynik to: {P[5][5]}'


print(funkcja2())
