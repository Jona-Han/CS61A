def ex_iter(list):
    index = 0
    def ex_next(list):
        nonlocal index
        index = index + 1
        return list[index-1]
    return ex_next