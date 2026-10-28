def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    global leaf_count
    if depth == target:
        leaf_count += 1
        return scores[index]
    if maxTurn:
        value = float('-inf')
        for i in range(2):
            value = max(value, alphabeta(
                depth + 1, index * 2 + i, False,
                scores, target, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for i in range(2):
            value = min(value, alphabeta(
                depth + 1, index * 2 + i, True,
                scores, target, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
scores = [3, 5, 2, 9, 3, 5, 2, 9]
depth = 3
leaf_count = 0
result = alphabeta(0, 0, True, scores, depth,
                   float('-inf'), float('inf'))
print("Alpha-Beta optimal value:", result)
print("Leaves evaluated:", leaf_count)
