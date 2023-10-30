"""
This module is an empty class 
"""
class OverrideMetaClass(type):
    """
    Override original inherited attributes from parent
    """
    def __dir__(cls) -> None:
        """
        control access to some inherited attributes
        """
        attributes = super().__dir__()
        n_attributes = []
        for attr in attributes:
            if attr != '__init_subclass__':
                n_attributes.append(attr)
        return n_attributes
"""
This is a a creation of BaseGeometry 
"""
class BaseGeometry(metaclass=OverrideMetaClass):
    """
    This is a a class with area method and integer validator
    integer validator args(value,name)
    These function must raise an exception 
    """ 
    def __dir__(cls) -> None:
        """
        control access to some inherited attributes
        """
        attributes = super().__dir__()
        n_attributes = []
        for attr in attributes:
            if attr != '__init_subclass__':
                n_attributes.append(attr)
        return n_attributes
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        name = ""
        if type(value) != int:
            raise Exception(f"{name} must be an integer")
        if value <= 0:
            raise Exception(f"{name} must be greater than 0")