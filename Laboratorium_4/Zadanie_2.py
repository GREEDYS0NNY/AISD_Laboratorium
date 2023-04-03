def Merge(A):
    if len(A) > 1:
        m = len(A) // 2
        l = A[:m]
        r = A[m:]

        Merge(l)
        Merge(r)

        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                A[k] = l[i]
                i += 1
            else:
                A[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            A[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            A[k] = r[j]
            j += 1
            k += 1

