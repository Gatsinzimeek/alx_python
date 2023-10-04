""" Square class
    Designed for diplay size of square
"""
class Square:
    """
    This method for intializing size of square to square attributes
    """
    def __init__(self,size=0):
            self.__size = size
    #this getter for retreive data from init method passed as an argument
    @property
    def size(self):
        return self.__size
    #this setter for rechanging of size attribute to value passed into when size method will be called
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """
    This method for diplaying area of square by adding size * size
    """
    def area(self):
        return self.__size **2
