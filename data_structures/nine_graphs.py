graph = {
    'A': ['B', 'C',],
    'B': ['A', 'D', 'E',],
    'C': ['A', 'F',],
    'D': ['B',],
    'E': ['B', 'F',],
    'F': ['C', 'E',],
}

print(graph)
# {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
print(graph['A'])
# ['B', 'C']
print(graph['C'])
# ['A', 'F']
print(graph['E'])
# ['B', 'F']