
import heapq
from collections import deque
graph = {
    "A": [("B", 1), ("C", 6)],
    "B": [("D", 2), ("E", 1)],
    "C": [("F", 2), ("G", 6)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}
def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None
def path_cost(path):
    total = 0
    for current, next_node in zip(path, path[1:]):
        for neighbor, cost in graph[current]:
            if neighbor == next_node:
                total += cost
                break
    return total
def uniform_cost_search(start, goal):
    frontier = [(0, start, [start])]
    best_cost = {start: 0}
    expanded = []
    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if cost > best_cost.get(node, float("inf")):
            continue
        expanded.append(node)
        if node == goal:
            return path, cost, expanded
        for neighbor, edge_cost in graph[node]:
            new_cost = cost + edge_cost
            if new_cost < best_cost.get(
                neighbor, float("inf")
            ):
                best_cost[neighbor] = new_cost
                heapq.heappush(
                    frontier,
                    (new_cost, neighbor, path + [neighbor])
                )
    return None, float("inf"), expanded
start, goal = "A", "G"
bfs_path = bfs(start, goal)
print("BFS path:", " -> ".join(bfs_path))
print("BFS path cost:", path_cost(bfs_path))
ucs_path, ucs_cost, expanded = uniform_cost_search(start, goal)
print("UCS path:", " -> ".join(ucs_path))
print("UCS path cost:", ucs_cost)
print("Verified UCS path cost:", path_cost(ucs_path))
print("UCS expanded order:", ", ".join(expanded))
