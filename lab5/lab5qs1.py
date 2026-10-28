import math
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # Base case: leaf node reached
    if curDepth == targetDepth:
        return scores[nodeIndex]
    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        )
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        )
scores = [3, 5, 2, 9, 0, 7]
treeDepth = math.ceil(math.log2(len(scores)))
scores += [0] * (2**treeDepth - len(scores))
print("Padded leaf scores:", scores)
print("Tree depth:", treeDepth)
print("The optimal value is:", minimax(0, 0, True, scores, treeDepth))
