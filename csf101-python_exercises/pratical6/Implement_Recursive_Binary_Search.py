def binary_search_recursive(arr, target ,left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
    
test_list = [1,2,3,4,5,6,7,8,9,10]
result = binary_search_recursive(test_list, 7, 0, len(test_list) - 1)
print(f"Recursive Binary Search: Index of 7 is {result}")