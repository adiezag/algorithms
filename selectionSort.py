def selectionSort(array):
    # Write your code here.

    # in this method, we assume that we have two defined portions in the array
    # the sorted and the unsorted
    # in every iteration we look for the current small number in the array and
    # place it in the sorted portion.
    # Nested for loop
    
    for i in range(len(array)-1):
        curSmallestIndex = i
        for j in range(i+1, len(array)):
            if array[j] < array[curSmallestIndex]:
                curSmallestIndex = j
        array[i], array[curSmallestIndex] = array[curSmallestIndex], array[i]

    return array
