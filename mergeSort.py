def mergeSort(ages):
    if len(ages) > 1:
        middleIndex = len(ages) // 2

        # Divide the array into two halves
        leftAges = ages[:middleIndex]
        rightAges = ages[middleIndex:]

        # Recursively sort the two halves
        mergeSort(leftAges)
        mergeSort(rightAges)

        # Merging the sorted halves
        i = j = k = 0

        while i < len(leftAges) and j < len(rightAges):
            if leftAges[i] < rightAges[j]:
                ages[k] = leftAges[i]
                i += 1
            else:
                ages[k] = rightAges[j]
                j += 1
            k += 1

        # Checking if any element was left in leftAges
        while i < len(leftAges):
            ages[k] = leftAges[i]
            i += 1
            k += 1

        # Checking if any element was left in rightAges
        while j < len(rightAges):
            ages[k] = rightAges[j]
            j += 1
            k += 1