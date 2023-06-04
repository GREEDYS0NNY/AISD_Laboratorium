import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def build_graph():
    print("1. Graf skierowany.\n"
          "2. Graf nieskierowany.\n"
          "3. Graf ważony")
    graph_type = int(input("Twój wybór: "))

    v = int(input("Podaj ilość wierzchołków: "))
    macierz = np.zeros((v, v))

    u = int(input("Podaj ilość połączeń: "))
    print("Podaj połączenia w formacie v, u, w:")
    for _ in range(u):
        connection = input().split()
        v_start = int(connection[0])
        v_end = int(connection[1])
        weight = 1
        if graph_type == 3:
            weight = int(connection[2])
        macierz[v_start][v_end] = weight
        if graph_type == 2:
            macierz[v_end][v_start] = weight

    print("Macierz sąsiedztwa:")
    print(macierz)

    adjacency_list = build_adjacency_list(macierz)
    print("Lista sąsiedztwa:")
    for vertex, neighbors in adjacency_list.items():
        print(f"{vertex}: {neighbors}")

    draw_graph(adjacency_list, graph_type)


def build_adjacency_list(adjacency_matrix):
    adjacency_list = {}
    v = len(adjacency_matrix)
    for vertex in range(v):
        neighbors = []
        for neighbor in range(v):
            if adjacency_matrix[vertex][neighbor] != 0:
                neighbors.append((neighbor, adjacency_matrix[vertex][neighbor]))
        adjacency_list[vertex] = neighbors
    return adjacency_list


def draw_graph(adjacency_list, graph_type):
    G = nx.DiGraph() if graph_type == 1 else nx.Graph()
    for vertex, neighbors in adjacency_list.items():
        for neighbor, weight in neighbors:
            G.add_edge(vertex, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=800, edge_color="gray")
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Graf")
    plt.show()


build_graph()
