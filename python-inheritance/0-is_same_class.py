"""
This is a module for performing instance checking 
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
    if isinstance(obj,a_class):
        return True
    else:
        return False