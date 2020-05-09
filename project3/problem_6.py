def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    maximum = None
    minimum = None

    for n in ints:
        if maximum is None or n > maximum:
            maximum = n

        if minimum is None or n < minimum:
            minimum = n

    return (minimum, maximum)

## Example Test Case of Ten Integers
import random


# Test case 1
# test for unsorted array
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test case 2
# test for empty array
l2 = []
print ("Pass" if ((None, None) == get_min_max(l2)) else "Fail")

# Test case 3
# test for array with all the same elements
l3 = [1,1,1,1,1,1,1,1,1,1,1,1,1]
print ("Pass" if ((1, 1) == get_min_max(l3)) else "Fail")
