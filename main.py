import os

def add(x, y):
    """Returns the sum of x and y."""
    if os.name == 'posix':
    	print("Line wont be reached on windows")
    	print("Another Line that wont be reached on windows")
    return x + y