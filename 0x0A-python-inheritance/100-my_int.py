#!/usr/bin/python3
"""
class MyInt that inherits from int
"""


class MyInt(int):
    def __init__(self, value):
        self.num = value

    def __eq__(self, value):
        return self.num != value

    def __ne__(self, value):
        return self.num == value
