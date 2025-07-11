# <---------------------- Depth First Search with Recursion (Stack)---------------------->
from collections import defaultdict

A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
D = defaultdict(list)

for u, v in A:
    D[u].append(v)
    
    
def dfs_recursive(node):
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)
            
source = 0
seen = set()
seen.add(source)

dfs_recursive(source)

# Time Complexity: O(E + V)