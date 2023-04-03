def SumaEl(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    else:
        m = n // 2
        l_suma = SumaEl(arr[:m])
        r_suma = SumaEl(arr[m:])
        return l_suma + r_suma
