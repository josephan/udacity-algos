def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # sort function using quick sort
    if len(input_list) == 0:
        return []

    quick_sort(input_list)

    a = 0
    a_len = 0
    b = 0
    b_len = 0

    if len(input_list) % 2 == 1 and len(input_list) >= 3:
        next_number = input_list.pop()
        a *= 10
        a += next_number
        a_len += 1
        next_number = input_list.pop()
        a *= 10
        a += next_number
        a_len += 1
        next_number = input_list.pop()
        b *= 10
        b += next_number
        b_len += 1

    while len(input_list) > 0:
        next_number = input_list.pop()
        if a_len == b_len:
            a *= 10
            a += next_number
            a_len += 1
        else:
            b *= 10
            b += next_number
            b_len += 1
    return [a, b]

def quick_sort(arr):
    recursive_quick_sort(arr, 0, len(arr) - 1)

def recursive_quick_sort(arr, start, end):
    if start >= end:
        return

    pivot_i = end
    left_i = start
    while left_i < pivot_i:
        pivot = arr[pivot_i]
        left = arr[left_i]
        if left >= pivot:
            arr[left_i] = arr[pivot_i-1]
            arr[pivot_i-1] = pivot
            arr[pivot_i] = left
            left_i = 0
            pivot_i -= 1
        else:
            left_i += 1

    recursive_quick_sort(arr, start, pivot_i-1)
    recursive_quick_sort(arr, pivot_i+1, end)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print(output)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test case 1
test_function([[1, 2, 3, 4, 5], [542, 31]])

# Test case 2
test_function([[9, 8], [9, 8]])

# Test case 3
test_function([[9, 8, 7], [98, 7]])

# Test case 4
test_function([[9, 8, 7, 6], [98, 76]])

# Test case 5
test_function([[9, 8, 7, 6, 5], [985, 76]])

# Test case 6
test_function([[9, 8, 7, 6, 5, 4, 3, 2, 1], [98541, 7632]])

# Test case 7
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Test case 8
test_function([[], []])
