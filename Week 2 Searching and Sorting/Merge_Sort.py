# <---------------------- Merge Sort ---------------------->
def merge_sort(arr):
    n = len(arr)
    
    if n <= 1:
        return arr
    
    m = n // 2
    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])
    
    sorted_array = []
    i = j = 0
    
    # Merge the sorted halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    # Append remaining elements (if any)
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array

# Test the function
A = [2, -3, 2, 3, 2, -5, 2, -3, 1, 7]
A = merge_sort(A)
print(A)


# Time Complexity: O(log n)
# Space Complexity: O(n) for the auxiliary array used in the merge step.