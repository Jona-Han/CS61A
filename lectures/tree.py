def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), "Branch is not a tree."
    return [label] + list(branches)
    
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

#Fibonacci Tree
def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

#Tree recursive structures can also be used to process trees
def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)

def increment_leaves(tree):
    """Return a tree like t with all leaves incremented by 1"""
    if is_leaf(tree):
        return tree(label(tree) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(tree)]
        return tree(label(tree), bs)

def increment(tree):
    """Return a tree with all labels incremented by 1"""
    return tree(label(tree) + 1, [increment(b) for b in branches(tree)])

#Creating a partition tree
def partition_tree(n, m):
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])


def print_tree(tree):
    """Prints all the values but doesn't indent"""
    print(label(tree))
    for b in branches(t):
        print_tree(b)

def print_tree_indented(tree, indent = 0):
    """Better print tree function that indents"""
    print("   " * indent + str(label(tree)))
    for b in branches(tree):
        print_tree_indented(b, indent + 1)

#Creating a tree recursive function to traverse the partition tree
def print_parts(tree, partition = []):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)

#Binarization of a tree. like slicing a tree if we want to place restrictions on the number of branches
def right_binarize(tree):
    """Construct a right-branching binary tree.
    Currently broken
    """
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]


