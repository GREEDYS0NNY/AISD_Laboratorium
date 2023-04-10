m = int(input('m: '))
n = int(input('n: '))
C = [[0 for j in range(m + 1)] for i in range(n + 1)]
for i in range(n + 1):
    C[i][0] = 1
for j in range(m + 1):
    C[j][j] = 1
for row in C:
    print(row)
