#!/usr/bin/python3
"""
class MyInt that inherits from int
"""


class MyInt(int):
    """
    class MyInt that inherits from int
    """
    def __init__(self, value):
        """ constructor """
        self.num = value

    def __eq__(self, value):
        """ equal change """
        return int.__ne__(self, value)

    def __ne__(self, value):
        """ non equal change """
        return int.__eq__(self, value)
