# <---------------------- Sorted case ---------------------->


# <---------------------- Approach 1. Via Recursion ---------------------->
def bSearch_rec(A, K, l, r):
    if (r - l == 0):
        return False
    mid = (l + r) // 2
    if (K == A[mid]):
        return True
    if (K < A[mid]):
        return bSearch_rec(A, K, l, mid)
    else:
        return bSearch_rec(A, K, mid + 1, r)
    
    
A = [5, 8, 12, 15, 21, 29, 38, 57]
n  = len(A)
l = 0
r = n - 1
K = 21
print(bSearch_rec(A, K, l, r))


# <---------------------- Approach 2. Via Loops ---------------------->
    # <----------------- Traditional Method ----------------->
    
def bsearch_trad(A, K):
    n = len(A)
    l = 0
    r = n - 1
    
    while l <= r:
        m = l + ((r - l) // 2)
        if A[m] == K:
            return True
        elif K < A[m]:
            r = m - 1
        else:
            l = m + 1
    return False

A = [-3, -2, 4, 15, 29, 89]
print(bsearch_trad(A, -2))

    # <----------------- Over - Under Method (Condition) ----------------->
    
def bsearch_condition(A):