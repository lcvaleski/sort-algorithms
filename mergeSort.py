def mergeSort(arr):
    if len(arr) > 1:
        middleIndex = len(arr) // 2

        # Divide the array into two halves
        leftHalf = arr[:middleIndex]
        rightHalf = arr[middleIndex:]

        # Recursively sort the two halves
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        # Merging the sorted halves
        i = j = k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1
            k += 1

        # Checking if any element was left in leftHalf
        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1

        # Checking if any element was left in rightHalf
        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1