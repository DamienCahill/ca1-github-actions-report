import os

def add(x, y):
    """Returns the sum of x and y."""
    if os.name != 'posix':
        print("Line wont be reached on Linux")
        print("Another Line that wont be reached on Linux")
    return x + y

def subtract(x, y):
    """Returns the x minus y."""
    return x - y