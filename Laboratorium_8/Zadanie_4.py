def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        min_distance = float('inf')
        min_vertex = None
        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        if min_vertex is None:
            break

        visited.add(min_vertex)

        for neighbor, weight in graph[min_vertex].items():
            distance = distances[min_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances


graph = {
    'A': {'B': 6, 'C': 3},
    'B': {'D': 2},
    'C': {'B': 1, 'D': 7},
    'D': {'E': 5},
    'E': {}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)

print(shortest_distances)
