def partition(arr, left, right):
    pivot = arr[right]  # Choose the last element as the pivot
    smaller_index = left  # the position of smaller elements
    
    for current_index in range(left, right):  
        if arr[current_index] <= pivot:  # If the current element is smaller than or equal to the pivot
            # Swap smaller element to the correct position
            arr[smaller_index], arr[current_index] = arr[current_index], arr[smaller_index]
            smaller_index += 1
    
    # Swap the pivot element to its correct position
    arr[smaller_index], arr[right] = arr[right], arr[smaller_index]
    return smaller_index


def kthSmallest(arr, left, right, k):
    if 0 < k <= right - left + 1:  # Check if k is within bounds
        pivot_index = partition(arr, left, right)  # Partition the array
        
        # Check if the pivot is the k-th smallest element
        if pivot_index - left == k - 1:
            return arr[pivot_index]
        
        # If pivot is too large, search the left subarray
        if pivot_index - left > k - 1:
            return kthSmallest(arr, left, pivot_index - 1, k)
        
        # If pivot is too small, search the right subarray
        return kthSmallest(arr, pivot_index + 1, right, k - pivot_index + left - 1)
    
    print("Index out of bounds")

# usage
arr = [3, 5, 1, 2, 4, 8, 0, -1, 7, 10]
n = len(arr)
k = 2
print("K-th smallest element is:", kthSmallest(arr, 0, n - 1, k))