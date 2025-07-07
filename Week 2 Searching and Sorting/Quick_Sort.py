# <---------------------- Quick Sort ---------------------->
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    p = arr[-1]
    l = [x for x in arr[:-1] if x <= p]
    r = [x for x in arr[:-1] if x > p]
    
    L = quick_sort(l)
    R = quick_sort(r)
    
    return L + [p] + R

A = [2, -3, 2, 3, 2, -5, 2, -3, 1, 7]
A = quick_sort(A)
print(A)

# Time Complexity: O(n Log n) {With Good Pivot} Worst Case: O(n ^ 2)
# Space Complexity: O(n)