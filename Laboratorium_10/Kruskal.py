G = [(4, 0, 1), (8, 0, 6), (8, 1, 2), (11, 1, 6), (7, 2, 3), (2, 2, 4), (4, 2, 8), (9, 3, 5), (14, 3, 8), (7, 4, 6),
     (6, 4, 7), (10, 5, 8), (8, 6, 0), (1, 6, 7), (2, 7, 8)]

GSorted = sorted(G, key=lambda x: x[0])

Connected = set()
Isolated = {}
T = []

for i in GSorted:
    if i[1] not in Connected or i[2] not in Connected:
        if i[1] not in Connected and i[2] not in Connected:
            Isolated[i[1]] = [i[1], i[2]]
            Isolated[i[2]] = Isolated[i[1]]
        else:
            if not Isolated.get(i[1]):
                Isolated[i[2]].append(i[1])
                Isolated[i[1]] = Isolated[i[2]]
            else:
                Isolated[i[1]].append(i[2])
                Isolated[i[2]] = Isolated[i[1]]

        T.append(i)
        Connected.add(i[1])
        Connected.add(i[2])

for i in GSorted:
    if i[2] not in Isolated[i[1]]:
        T.append(i)
        temporary = Isolated[i[1]]
        Isolated[i[1]] += Isolated[i[2]]
        Isolated[i[2]] += temporary

print(T)
