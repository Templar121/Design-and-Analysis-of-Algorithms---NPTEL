# <---------------------- Sorted case ---------------------->


# <---------------------- Approach 1. Via Recursion ---------------------->
def bSearch_rec(A, K, l, r):
    if (r - l == 0):
        return False
    mid = (l + r) // 2
    if (K == A[mid]):
        return True
    if (K < A[mid]):
        return bSearch(A, K, l, mid)
    else:
        return bSearch(A, K, mid + 1, r)
    
    
A = [5, 8, 12, 15, 21, 29, 38, 57]
n  = len(A)
l = 0
r = n - 1
K = 21
print(bSearch_rec(A, K, l, r))


# <---------------------- Approach 2. Via Loops ---------------------->