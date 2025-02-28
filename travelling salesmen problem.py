from itertools import permutations

def tsp(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_path = float('inf')
    best_route = None
    
    for perm in permutations(vertices):
        current_path = 0
        current_node = start
        
        for node in perm:
            current_path += graph[current_node][node]
            current_node = node
        
        current_path += graph[current_node][start]
        
        if current_path < min_path:
            min_path = current_path
            best_route = (start,) + perm + (start,)
    
    return best_route, min_path

# Example usage
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

start_node = 'A'
route, cost = tsp(graph, start_node)
print(f"Optimal route: {route} with cost {cost}")
