def dz_na_bn(i):
    if i == 0:
        return "0"
    elif i == 1:
        return "1"
    else:
        return dz_na_bn(i // 2) + str(i % 2)


print(dz_na_bn(3))
