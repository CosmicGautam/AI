graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': ['I'],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}
visited = set()
goal_reached = False
def dfs(visited, graph, node, goal):
    global goal_reached
    if goal_reached:
        return
    
    if node not in visited:
        print(node, end='->' if node != goal else '')
        visited.add(node)
        if node == goal:
            goal_reached = True
            return
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, goal)
goal_node = input("Enter the goal node for DFS traversal: ")
print(f"Following is the Depth-First Search to goal '{goal_node}'")
dfs(visited, graph, 'A', goal_node)
