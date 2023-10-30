"""
This is a a creation of BaseGeometry 
"""
class BaseGeometry:
    """
    This is a a class with area method and integer validator
    integer validator args(value,name)
    These function must raise an exception 
    """ 
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        name = ""
        if type(value) != int:
            raise Exception(f"{name} must be an integer")
        if value <= 0:
            raise Exception(f"{name} must be greater than 0")