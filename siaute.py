def find_peak(arr):
    for i in range(len(arr)):
        if i == 0 and arr[i] > arr[i+1]:
            return i
        elif i == len(arr)-1 and arr[i] > arr[i-1]:
            return i
        elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            return i
    return -1  # If no peak element is found

# Example usage
arr = [1, 3, 4, 5, 2]
peak_index = find_peak(arr)
print("The index of the first peak element is:", peak_index)
