"""
This is a module for performing instance checking 
"""
# This is function use to check if instate of class
def is_same_class(obj, a_class):
    if isinstance(obj,a_class):
        return True
    else:
        return False