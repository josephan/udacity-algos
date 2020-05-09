def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0:
        return 0
    if number == 1:
        return 1
    root = 0
    upper = number
    lower = 0
    while lower <= upper:
        mid = (upper + lower) // 2
        square = mid * mid
        if square == number:
            return mid
        if square < number:
            lower = mid + 1
            root = mid
        else:
            upper = mid - 1
    return root

# Test case 1
print ("Pass" if  (3 == sqrt(9)) else "Fail")
# Test case 2
print ("Pass" if  (0 == sqrt(0)) else "Fail")
# Test case 3
print ("Pass" if  (4 == sqrt(16)) else "Fail")
# Test case 4
print ("Pass" if  (1 == sqrt(1)) else "Fail")
# Test case 5
print ("Pass" if  (5 == sqrt(27)) else "Fail")
# Test case 6
print ("Pass" if  (10 == sqrt(100)) else "Fail")
# Test case 7
print ("Pass" if  (100 == sqrt(10000)) else "Fail")
# Test case 8
print ("Pass" if  (1000 == sqrt(1000000)) else "Fail")
# Test case 9
print ("Pass" if  (10000 == sqrt(100000000)) else "Fail")
