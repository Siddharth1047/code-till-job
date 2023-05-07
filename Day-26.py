# Day 23, 24 and 25 were revision days

# Day -26 is DFS & BFS
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        visited.add(node)
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Read input from file and construct undirected graph
graph = {}
with open("bst.txt", "r") as file:
    for line in file:
        u, v = map(int, line.strip().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

print("BFS traversal: ", end='')
bfs(graph, 1)
print("\nDFS traversal: ", end='')
dfs(graph, 1)
"""
I'm taking input from a file names "bst.txt"
with contents: -
1 2
1 3
2 4
2 5
3 6
3 7
4 8
5 8
6 8
7 8
"""