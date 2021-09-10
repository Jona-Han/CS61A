empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair"""
    return s == 'empty' or (len(s) == 2 and is_link(s[1]))

#Constructor function for a linked lists
def link(first, rest):
    """Construct a linked list using its first element and its rest"""
    assert is_link(rest), "Rest must be a linked list"
    return [first, rest]

#First and rest are selector functions
def first(s):
    """Return first element of a linked list"""
    assert is_link(s), "First only applies to linked lists"
    assert s != empty, "Empty linked list has no first element"
    return s[0]

def rest(s):
    """Return rest of the elements of a linked list"""
    assert is_link(s), "Rest only appplies to linked lists"
    assert s != empty, "Empty linked list has no rest"
    return s[1]

def len_link(s):
    """Returns the length of a linked list"""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

def getitem_link(s, i):
    """Return the element at index i of linked list  s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

def len_link_recursive(s):
    """Returns length of a linked list but recursively"""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))

def getitem_link_recursive(s, i):
    """getitem_link function but recursive"""
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)

def extend_link(s, t):
    """Return a list with elements of s followed by elements of t"""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))

def apply_to_all_link(f, s):
    """Apply f to each element of s"""
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))

def keep_if_link(f, s):
    """Return a list with elements of s for which f(s) is true"""
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept

def join_link(s, separator):
    """Return a string of all elements in s separated by a separator"""
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)
    
def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return link(empty, empty) # A list containing the empty partition
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = partitions(n-m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)

def print_partitions(n, m):
    lists = partitions(n, m)
    strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))