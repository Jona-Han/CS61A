def count_partitions(n, t):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif t == 0:
        return 0
    else:
        return count_partitions(n, t-1) + count_partitions(n-t, t)
