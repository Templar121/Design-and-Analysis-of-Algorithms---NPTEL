# <---------------------- Unsorted case ---------------------->

def lSearch(A, K):
    i = 0
    n = len(A)
    while i < n and A[i] != K:
         i = i + 1
    if i < n:
        return i # Found i --> index
    else:
        return -1 # Not Found
    
    
A = [5, 10, 90, 1, 2, 7, 5]
K= 90
print(lSearch(A, K))



# Time Complexity: O(N)