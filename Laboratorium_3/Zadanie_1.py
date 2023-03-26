# forma iteracyjna
def nwd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


print(nwd(12, 17))
print(nwd(28, 24))


# forma rekurencyjna
def nwdrek(a, b):
    if a != b:
        if a > b:
            return nwdrek(a - b, b)
        else:
            return nwdrek(a, b - a)
    return a


print(nwd(12, 17))
print(nwd(28, 24))


#  optymalna forma iteracyjna

def nwd2(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


print(nwd2(12, 18))


# optymalna forma rekurencyjna

def nwd2rek(a, b):
    if b != 0:
        return nwd2rek(b, a % b)
    return a


print(nwd2rek(12, 18))
