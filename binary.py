def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr = [1, 3, 4, 5, 7, 9, 11]
target = 5
index = binary_search(arr, target)
print(index) # Shows index of 5 in the list