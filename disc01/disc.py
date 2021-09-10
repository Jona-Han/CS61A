def wears_jacket_with_if(temp, raining):
    """Returns a boolean whether Alfonso will wear a jacket.
    
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining:
        return True
    else:
        return False

def wears_jacket(temp, raining):
    """Returns a boolean like above but in one line

        >>> wears_jacket(90, False)
        False
        >>> wears_jacket(40, False)
        True
        >>> wears_jacket(100, True)
        True
    """
    return temp < 60 or raining

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """

    counter = 2
    while counter < n:
        if n % counter == 0:
            return False
        counter += 1
    return True
            
    