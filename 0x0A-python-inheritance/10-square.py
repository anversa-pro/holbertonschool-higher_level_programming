#!/usr/bin/python3
"""
Create a subclass
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Subclass Rectangle inheritated of BaseGometry
    """

    def __init__(self, size):
        self.integer_validator("width", size)
        self.__size = size
        super().__init__(size, size)
    
    def area(self):
        return self.__size * self.__size