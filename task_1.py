def find_min_max(arr):
    # If the array has only one element
    if len(arr) == 1:
        return (arr[0], arr[0])
    
    # If the array has two elements
    elif len(arr) == 2:
        if arr[0] < arr[1]:
            return (arr[0], arr[1])
        else:
            return (arr[1], arr[0])
    
    else:
        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively find min and max in the left half
        left_min, left_max = find_min_max(left_half)
        
        # Recursively find min and max in the right half
        right_min, right_max = find_min_max(right_half)
        
        # Combine the results
        overall_min = left_min if left_min < right_min else right_min
        overall_max = left_max if left_max > right_max else right_max
        
        return (overall_min, overall_max)

if __name__ == "__main__":
    sample_array = [3, 5, 1, 2, 4, 8, 0, -1, 7, 10]
    minimum, maximum = find_min_max(sample_array)
    print(f"Minimum element: {minimum}")
    print(f"Maximum element: {maximum}")
