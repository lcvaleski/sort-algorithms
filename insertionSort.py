import utils.swap as swap

def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j]:
            swap(arr, j - 1, j)
            j -= 1