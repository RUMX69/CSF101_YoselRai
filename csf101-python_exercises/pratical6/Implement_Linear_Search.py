def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

test_list = [2,5,7,5,2,5,6,3,26,7,8,8,]
result = linear_search(test_list, 26)
print(f"Linear Search: Index of 26 is {result}")
