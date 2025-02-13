def mergeSort(array):
    # Write your code here.
    if len(array) == 1:
        return array

    middle = len(array) // 2

    leftHalf = array[:middle]
    print(leftHalf)
    rightHalf = array[middle:]
    print(rightHalf)

    
    return mergeSortedArray(mergeSort(leftHalf),mergeSort(rightHalf))
    


def mergeSortedArray(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf)+len(rightHalf))
    k = 0
    i = 0
    j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k += 1
    while i < len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1

    while j < len(rightHalf):
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1
    print('sorted array: ', sortedArray)
    return sortedArray
    
