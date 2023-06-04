from collections import deque


def bfs(G, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        print(vertex)

        if vertex not in visited:
            visited.add(vertex)
            neighbors = G[vertex]

            for neighbor, is_connected in enumerate(neighbors):
                if is_connected and neighbor not in visited:
                    queue.append(neighbor)


G = [
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1]
]

bfs(G, 0)
