# <---------------------- Insertion Sort ---------------------->
# <---------------------- Approach 1. Via Loops ---------------------->
def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if A[j - 1] > A[j]:
                A[j - 1], A[j] = A[j], A[j - 1]
            else:
                break


A = [-5, 3, 2, 1, -3, -3, 7, 2, 2, 2]
insertion_sort(A)
print(A)


# <---------------------- Approach 2. Recursion ---------------------->
def insertion_sort_rec(A, start):
    n = len(A)
    if start >= n - 1:
        return 
    insert(A, start)
    insertion_sort_rec(A, start + 1)
    return 

def insert(A, start): # Helper Function for Insertion
    pos = start
    while pos > 0 and (A[pos] < A[pos - 1]):
        A[pos], A[pos - 1] = A[pos - 1], A[pos]
        pos = pos - 1
        
        
A = [2, -3, 2, 3, 2, -5, 2, -3, 1, 7]
insertion_sort_rec(A, start = 0)
print(A)
# Time Complexity: O(N ^ 2)
# Space Complexity: O(1) (In-place sorting)