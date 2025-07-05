# <---------------------- Insertion Sort ---------------------->

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


# Time Complexity: O(N ^ 2)
# Space Complexity: O(1) (In-place sorting)