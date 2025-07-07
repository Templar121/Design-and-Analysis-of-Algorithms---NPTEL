# <---------------------- Merge Sort ---------------------->
def counting_sort(A):
    n = len(A)
    maxx = max(A)
    count = [0] * (maxx + 1)
    
    for x in A:
        count[x] += 1
        
    i = 0
    for c in range(maxx + 1):
        while count[c] > 0:
            A[i] = c
            i += 1
            count[c] -= 1

A = [2, 3, 2, 3, 2, 5, 2, 3, 1, 7]
counting_sort(A)
print(A)