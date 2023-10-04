""" Square class
    Designed for diplay size of square
"""
class Square:
    """
    This method for intializing size of square to square attributes
    """
    def __init__(self,size=0):
        if not isinstance(size,int):
            raise TypeError('size must be an integer')
        if not size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    """
    This method for diplaying area of square by adding size * size
    """
    def area(self):
        return self.__size **2