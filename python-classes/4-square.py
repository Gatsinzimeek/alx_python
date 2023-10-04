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
    #this getter for retreive data from init method passed as an argument
    @property
    def size(self):
        return self.__size
    #this setter for rechanging of size attribute to value passed into when size method will be called
    @size.setter
    def size(self, value):
        self.__size = value
    """
    This method for diplaying area of square by adding size * size
    """
    def area(self):
        return self.__size * self.__size
    """
    This method for diplaying square shape using # based on size entered as argument
    """
    def my_print(self):
        if self.__size > 0:
            for i  in range(self.__size):
                print('#')
                for j in range(i):
                    print('#')
        else:
            print('')