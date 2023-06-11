import math


def get_min(G, Isolated):
    minimum = (math.inf, -1, -1)
    for v in Isolated:
        krawedz = min(G, key=lambda x: x[0] if (x[1] == v or x[2] == v) and (
                x[1] not in Isolated or x[2] not in Isolated) else math.inf)
        if minimum[0] > krawedz[0]:
            minimum = krawedz
    return minimum


G = [(math.inf, -1, -1), (4, 0, 1), (8, 0, 6), (8, 1, 2), (11, 1, 6), (7, 2, 3), (2, 2, 4), (4, 2, 8), (9, 3, 5),
     (14, 3, 8),
     (7, 4, 6),
     (6, 4, 7), (10, 5, 8), (8, 6, 0), (1, 6, 7), (2, 7, 8)]

N = 9
Isolated = {1}
T = []

while len(Isolated) < N:
    min_krawedz = get_min(G, Isolated)
    if min_krawedz[0] == math.inf:
        break

    T.append(min_krawedz)
    Isolated.add(min_krawedz[1])
    Isolated.add(min_krawedz[2])

print(T)
