graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
def dls(node, goal, limit, path=None):
    if path is None:
        path = [node]
    if node == goal:
        return "FOUND", path
    cutoff = False
    if limit == 0:
        return ("CUTOFF", None) if graph[node] else ("FAILURE", None)
    for child in graph[node]:
        if child in path:
            continue
        status, result = dls(child, goal, limit - 1, path + [child])
        if status == "FOUND":
            return status, result
        if status == "CUTOFF":
            cutoff = True
    return ("CUTOFF", None) if cutoff else ("FAILURE", None)
def iddfs(start, goal, max_depth):
    attempted_limits = []
    for depth in range(max_depth + 1):
        attempted_limits.append(depth)
        status, path = dls(start, goal, depth)
        print(f"Depth {depth}: {status}; Path: {path}")
        if status == "FOUND":
            print("Limits attempted:", attempted_limits)
            return path
    print("Limits attempted:", attempted_limits)
    return None
if __name__ == "__main__":
    print("DLS RESULTS (start=A, goal=G)")
    for limit in range(1, 5):
        status, path = dls("A", "G", limit)
        print(f"Limit {limit}: {status}; Path: {path}")
    print("\nIDDFS RESULTS (maximum depth=4)")
    iddfs("A", "G", 4)

