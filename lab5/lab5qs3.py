
def minimax(node, depth, maximizing, leaf_counter):
    if depth == 0:
        leaf_counter[0] += 1
        return node
    if maximizing:
        best = float("-inf")
        for child in node:
            value = minimax(child, depth - 1, False, leaf_counter)
            best = max(best, value)
        return best
    else:
        best = float("inf")
        for child in node:
            value = minimax(child, depth - 1, True, leaf_counter)
            best = min(best, value)
        return best
def alpha_beta(node, depth, alpha, beta, maximizing, leaf_counter):
    if depth == 0:
        leaf_counter[0] += 1
        return node
    if maximizing:
        best = float("-inf")
        for child in node:
            value = alpha_beta(
                child, depth - 1, alpha, beta, False, leaf_counter
            )
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break
        return best
    else:
        best = float("inf")
        for child in node:
            value = alpha_beta(
                child, depth - 1, alpha, beta, True, leaf_counter
            )
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
tree_A = [
    [3, 5],
    [2, 9],
    [3, 5],
    [2, 9]
]
tree_B = [
    [9, 3],
    [5, 2],
    [9, 3],
    [5, 2]
]
def run_test(tree, name):
    minimax_count = [0]
    alpha_beta_count = [0]
    minimax_value = minimax(tree, 2, True, minimax_count)
    alpha_beta_value = alpha_beta(
        tree, 2, float("-inf"), float("inf"),
        True, alpha_beta_count
    )
    print(f"\n{name}")
    print("Minimax value:", minimax_value)
    print("Minimax leaves evaluated:", minimax_count[0])
    print("Alpha-Beta value:", alpha_beta_value)
    print("Alpha-Beta leaves evaluated:", alpha_beta_count[0])
    print("Same final value:", minimax_value == alpha_beta_value)
run_test(tree_A, "Branch Ordering A")
run_test(tree_B, "Branch Ordering B")
