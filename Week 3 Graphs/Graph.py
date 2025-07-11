# <---------------------- Graphs ---------------------->
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        
    def __str__(self):
        return f"Node({self.value})"
    
    def display(self):
        connections = [node.value for node in self.neighbors]
        return f"{self.value} is connected to: {connections}"
    
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')

A.neighbors.append(B)
B.neighbors.append(A)

C.neighbors.append(D)
D.neighbors.append(C)

print(A.display())