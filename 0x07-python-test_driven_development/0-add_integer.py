
def add_integer(a, b=98):
    """A function that adds two integers

    Args:
        a (int/ float): integer to be added
        b (int/ float): integer to be added with default value 98
        """
    
    if not isinstance(a, int) or not isinstance(a, float):
        """a must be an int or float else raise TypeError"""
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or not isinstance(b, float):
        """b must be an int or float else raise TypeError"""
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
