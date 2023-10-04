""" Square class
    Designed for diplay size of square
"""
class Square:
    """
    This method for intializing size of square to square attributes
    """
    def __init__(self,size=0):
        if(type(size) == int and size >= 0):
            self.__size = size
        else:
            print('size must be an integer')
            print('size must be >= 0')