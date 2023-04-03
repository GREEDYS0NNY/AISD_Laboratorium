def MaxEl(wektor):
    n = len(wektor)
    if n == 1:
        return wektor[0]
    else:
        m = n // 2
        l_max = MaxEl(wektor[:m])
        r_max = MaxEl(wektor[m:])
        return max(l_max, r_max)
