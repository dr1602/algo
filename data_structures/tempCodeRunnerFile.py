graph = {
    'A': ['B', 'C',],
    'B': ['A', 'D', 'E',],
    'C': ['A', 'F',],
    'D': ['B',],
    'E': ['B', 'F',],
    'F': ['C', 'E',],
}

print(graph)
print(graph['A'])
print(graph['C'])
print(graph['E'])