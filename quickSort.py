def quickSort(array):
    # Write your code here.
    partition(array, 0, len(array)-1)
    return array


def partition(array, s, e):
    if s >= e:
        return
    pivot = array[s]
    leftIdx = s
    rightIdx = e
    
    while leftIdx < rightIdx:
        
        while leftIdx <=e and array[leftIdx] <= pivot:
            
            leftIdx += 1
        while rightIdx >= s and array[rightIdx] > pivot:
            rightIdx -= 1
        if leftIdx < rightIdx:
            array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
    array[s], array[rightIdx] = array[rightIdx], array[s]        
    partition(array, s, rightIdx-1)
    partition(array, rightIdx+1, e)
