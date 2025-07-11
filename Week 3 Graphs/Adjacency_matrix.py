# <---------------------- Array of Edges (Directed) [start, End] to Adjacency Matrix ---------------------->
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
n = 8
m = []

for i in range(n):
    m.append(([0] * n))
    
for u, v in A:
    m[u][v] = 1
    
print(m)