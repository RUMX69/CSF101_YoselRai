def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

test_list = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(test_list, 7)
print(f"Binary Search: Index of 7 is {result}")