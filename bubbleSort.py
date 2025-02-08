def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-1-i):
            if array [j +1] < array [j]:
                array[j], array[j+1] = array[j+1], array[j]

    return array
