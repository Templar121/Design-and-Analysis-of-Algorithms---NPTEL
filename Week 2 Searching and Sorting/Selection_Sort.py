# <---------------------- Selection Sort ---------------------->

def selection_sort(A):
    n = len(A)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
        
A = [-5, 3, 2, 1, -3, -3, 7, 2, 2, 2]
selection_sort(A)

print(A)


# Time Complexity: O(N ^ 2)
# Space Complexity: O(1) (In-place sorting)