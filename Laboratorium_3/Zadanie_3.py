def f(i):
    if i == 1:
        return 4
    else:
        return 1 / (1 - f(i - 1))


print(f(8))  # F
print(f(9))  # P
print(f(10))  # P
print(f(100))  # F
