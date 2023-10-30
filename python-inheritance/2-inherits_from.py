"""
This is a a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False 
"""
def inherits_from(obj, a_class):
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
    
    return issubclass(any_class, a_class) and any_class is not a_class