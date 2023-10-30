"""
This is a method for performing instance checking 
"""
def is_kind_of_class(obj, a_class):
    """
    checking if an object recieved is and instance of a_class

    Parameters:
    obj : The number.
    a_class: the class.

    Returns:
    True if is an instance 
    False if is not and instance
    """
    any_class = type(obj)

    if issubclass(any_class, a_class) == True:
        return True
    else:
        return False