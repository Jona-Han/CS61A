def mysum(n):
    """Calculates sum.
    
    >>> mysum(5)
    15
    """
    if n == 0:
        return 0
    else:
        return n + mysum(n-1)





