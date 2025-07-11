# <---------------------- Convert an array of edges into Adjacency Lists ---------------------->
from collections import defaultdict

A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
D = defaultdict(list)

for u, v in A:
    D[u].append(A)