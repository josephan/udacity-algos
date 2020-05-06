def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    zero_to_half_of_number = list(range((number+1//2)+1))
    return _sqrt(number, zero_to_half_of_number)

def _sqrt(number, numbers):
    if len(numbers) == 1:
        return numbers[0]

    mid = (len(numbers)-1)//2
    square = numbers[mid] * numbers[mid]

    if square == number:
        return numbers[mid]
    elif square > number:
        return _sqrt(number, numbers[0:mid])
    else:
        return _sqrt(number, numbers[mid:len(numbers)])



print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
