graph = {
  "a": ["b", "c", "d"],
  "b": ["a", "d"],
  "c": ["a", "d", "f"],
  "d": ["a", "b", "c", "e"],
  "e": ["d", "f"],
  "f": ["c","d"],
}

[]

# [2, [a, c, d]]

def shortest_path(graph, start, mid, end):
    
    start_to_mid = shortest_path_help(graph, start, mid)
    # a = list(reversed(start_to_mid))
    # a.pop()
    
    # mid_to_end = shortest_path_help(graph, mid, end)
    # b = list(reversed(mid_to_end))
    # direction = a + b
    # return [len(direction)-1, direction]
    
def shortest_path_help(graph, start, end):
    trajectory = []
    queue = [start]
    parent = {}
    visited = [start]
    dist_to_root = {start:0}
    
    while queue:
        current_node = queue.pop(0)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                parent[neighbor] = current_node
                queue.append(neighbor)
                visited.append(neighbor)
                dist_to_root[neighbor] = dist_to_root[current_node] + 1
    current = end    
    while current != start:
        trajectory.append(current)
        current = parent[current]
    trajectory.append(current)
    print(dist_to_root)
    print(dist_to_root["f"])
    return trajectory
    
print(shortest_path(graph, 'a', 'c', 'd'))
    # parent
    # {   b:a
    #     c:a
    #     d:a
    #     }
    