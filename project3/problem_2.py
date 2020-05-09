def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1
    return rotated_binary_search(input_list, number, 0, len(input_list)-1)

def rotated_binary_search(arr, target, lower, upper):
    mid = (upper + lower) // 2

    if arr[mid] == target:
        return mid

    if lower >= upper:
        return -1

    if arr[mid] < arr[upper]:
        if arr[mid] < target <= arr[upper]:
            return rotated_binary_search(arr, target, mid+1, upper)
        else:
            return rotated_binary_search(arr, target, lower, mid-1)
    else:
        if arr[lower] <= target < arr[mid]:
            return rotated_binary_search(arr, target, lower, mid-1)
        else:
            return rotated_binary_search(arr, target, mid+1, upper)

# Tests

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Test case 1
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])

# Test case 2
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])

# Test case 3
test_function([[6, 7, 8, 1, 2, 3, 4], 8])

# Test case 4
test_function([[6, 7, 8, 1, 2, 3, 4], 1])

# Test case 5
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Test case 6
test_function([[], -1])

# Test case 7
test_function([[0], -1])

# Test case 7
test_function([[1,2,3,4,5,6,7,8,9], 5])
