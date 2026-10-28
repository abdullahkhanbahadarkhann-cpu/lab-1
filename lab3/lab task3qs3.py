
from collections import deque
import heapq

# Weighted graph: (neighbour, edge_cost)
graph = {
    "A": [("B", 1), ("C", 6)],
    "B": [("D", 2), ("E", 1)],
    "C": [("F", 2), ("G", 6)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}


# Breadth-First Search
def bfs(start, goal):
    queue = deque([(start, [start])])
    seen = {start}

    while queue:
        node, path = queue.popleft()

        if node == goal:
            return path

        for neighbour, cost in graph[node]:
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return None


# Uniform Cost Search
def ucs(start, goal):
    # (total_cost, tie_breaker, node, path)
    frontier = [(0, 0, start, [start])]
    best_cost = {start: 0}
    counter = 1
    processing_order = []

    while frontier:
        cost, order, node, path = heapq.heappop(frontier)

        # Skip outdated entries
        if cost != best_cost.get(node):
            continue

        processing_order.append(node)

        if node == goal:
            return path, cost, processing_order

        for neighbour, edge_cost in graph[node]:
            new_cost = cost + edge_cost

            if new_cost < best_cost.get(neighbour, float("inf")):
                best_cost[neighbour] = new_cost

                heapq.heappush(
                    frontier,
                    (new_cost, counter, neighbour,
                     path + [neighbour])
                )
                counter += 1

    return None, float("inf"), processing_order


# Independently calculate path cost
def path_cost(path):
    total = 0

    for a, b in zip(path, path[1:]):
        total += next(
            cost for neighbour, cost in graph[a]
            if neighbour == b
        )

    return total


# Main program
if __name__ == "__main__":
    bfs_path = bfs("A", "G")
    ucs_path, ucs_total, ucs_order = ucs("A", "G")

    print("BFS path:", " -> ".join(bfs_path))
    print("BFS hop count:", len(bfs_path) - 1)
    print("BFS path cost:", path_cost(bfs_path))

    print("UCS path:", " -> ".join(ucs_path))
    print("UCS total cost:", ucs_total)
    print("UCS processing order:", " -> ".join(ucs_order))
    print("UCS cost independently checked:", path_cost(ucs_path))
