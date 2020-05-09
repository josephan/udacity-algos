def sort_012(arr):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       arr(list): List to be sorted
    """
    low = 0
    mid = 0
    high = len(arr)-1

    while mid <= high:
        if arr[mid] == 2:
            arr[mid] = arr[high]
            arr[high] = 2
            high -= 1
        elif arr[mid] == 0:
            arr[mid] = arr[low]
            arr[low] = 0
            mid += 1
            low += 1
        else:
            mid += 1
    return arr

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Test case 1
test_function([])
# Test case 2
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# Test case 3
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# Test case 4
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
