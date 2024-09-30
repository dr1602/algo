import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        dist, node = heapq.heappop(queue)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node].items():
            new_dist = dist + weight
            if new_dist < distances[neighbor]:

                distances[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))
    return distances

# Ejemplo 1: Grafo simple
graph1 = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 3, 'E': 1},
    'C': {'B': 1, 'D': 5},
    'D': {'E': 2},
    'E': {}
}

print("Ejemplo 1:")
print(dijkstra(graph1, 'A'))

# Ejemplo 2: Grafo más complejo
graph2 = {
    'S': {'A': 4, 'B': 2},
    'A': {'B': 1, 'C': 5},
    'B': {'A': 1, 'C': 8, 'D': 10},
    'C': {'D': 2, 'E': 6},
    'D': {'E': 3},
    'E': {}
}

print("\nEjemplo 2:")
print(dijkstra(graph2, 'S'))

# Ejemplo 3: Grafo con ciclos
graph3 = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 3, 'C': 1},
    'C': {'B': 1, 'D': 5},
    'D': {'A': 7, 'E': 2},
    'E': {'A': 6}
}

print("\nEjemplo 3:")
print(dijkstra(graph3, 'A'))

'''
Ejemplo 1:
{'A': 0, 'B': 3, 'C': 2, 'D': 6, 'E': 4}

Ejemplo 2:
{'S': 0, 'A': 3, 'B': 2, 'C': 8, 'D': 10, 'E': 13}

Ejemplo 3:
{'A': 0, 'B': 3, 'C': 2, 'D': 6, 'E': 8}
'''