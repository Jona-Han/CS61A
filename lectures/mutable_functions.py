def make_withdraw(balance):
    """Function that stores the balance using nonlocal assignment
    and uses the concept of persistent local state
    """
    def withdraw(value):
        nonlocal balance
        if value > balance:
            return "Insufficient Funds."
        balance = balance - value
        return balance
    return withdraw

def make_withdraw_list(balance):
    """Like above function but uses a nonlocal list. 
    Remember that lists are mutable
    """
    b = [balance]
    def withdraw(value):
        if value > b[0]:
            return "Insufficient Funds."
        b[0] = b[0] - amount
        return b[0]
    return withdraw

#Example of a function that is not referentially transparent
def f(x):
    """Usage:
    a = f(1)
    b = a(2)
    total = b(3) + b(4)
    """
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g