"""
This is a a creation of BaseGeometry 
"""
class BaseGeometry():
    """
    This is a a class with holding nothing
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