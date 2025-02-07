# recursive method

def binarySearch(arr, target, left, right):
    print('calling function')
    if left > right:
        print('done')
        return False

    mid = (left + right) // 2

    if arr[mid] == target:
        print('found')
        return True
    elif target < arr[mid]:
        return binarySearch(arr, target, left, mid - 1)
    elif target > arr[mid]:
        return binarySearch(arr, target, mid + 1, right)
    

# iterative method
# def binarySearch(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left+right) // 2
#         if target == arr[mid]:
#             return True
#         elif target < arr[mid]:
#             right = mid - 1
#         elif target > arr[mid]:
#             left = mid + 1
#         print("left: ", left, "right: ", right)
    
#     return False

arr = [2,3,4,10,40]
target = 10
# print(binarySearch(arr, target))
l, r = 0, len(arr) - 1
print(binarySearch(arr, target, l, r))
