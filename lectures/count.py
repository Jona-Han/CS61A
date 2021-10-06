def count(f):
    """Counts the number of times a function is called."""
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

def memo(f):
    """This speeds up the time it takes for a function is called by keeping known values stored in a cache"""
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

@memo
def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n-2) + fib(n-1)

