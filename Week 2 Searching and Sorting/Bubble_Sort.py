# <---------------------- Bubble Sort ---------------------->

def bubble_sort(A):
    n = len(A)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if A[i - 1] > A[i]:
                flag = True
                A[i - 1], A[i] = A[i], A[i - 1]
                
A = [-5, 3, 2, 1, -3, -3, 7, 2, 2, 2]
bubble_sort(A)

print(A)