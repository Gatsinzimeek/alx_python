"""
This is a method for performing instance checking 
"""
def is_same_class(obj, a_class):
    """
    checking if an object recieved is and instance of a_class

    Parameters:
    obj : The number.
    a_class: the class.

    Returns:
    True if is an instance 
    False if is not and instance
    """
    return type(obj) is a_class