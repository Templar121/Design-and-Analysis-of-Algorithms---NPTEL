# <---------------------- Depth First Search with Iteration (Stack) ---------------------->
from collections import defaultdict

A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
D = defaultdict(list)

for u, v in A:
    D[u].append(v)
    
source = 0
seen = set()
seen.add(source)
stack = [source]

while stack:
    node = stack.pop()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node)
            

# Time Complexity: O(E + V)