import utils.swap as swap

def partition(arr, low, high):
    
    # Choose the pivot
    pivot = arr[high]
    
    # Index of smaller element and indicates 
    # the right position of pivot found so far
    i = low - 1
    
    # Traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to 
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap.swap(arr, i, j)
    
    # Move pivot after smaller elements and
    # return its position
    swap.swap(arr, i + 1, high)
    return i + 1