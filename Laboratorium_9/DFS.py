class Vertex:
    def __init__(self):
        self.p = -1
        self.visited = False
        self.time_1 = 0
        self.time_2 = 0


def DFS(G):
    V = len(G)
    visited = [False] * V
    parent = [-1] * V
    time = 0

    for u in range(V):
        if not visited[u]:
            time = DFS_Explore(G, u, visited, parent, time)
    return time


def DFS_Explore(G, u, visited, parent, time):
    time += 1
    u_time_1 = time
    visited[u] = True

    for v in range(len(G[u])):
        if G[u][v] == 1 and not visited[v]:
            parent[v] = u
            time = DFS_Explore(G, v, visited, parent, time)

    time += 1
    u_time_2 = time
    return time


G = [
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0]
]

print(DFS(G))
