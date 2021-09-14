#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    number_to_compare = my_list[0]
    for i in my_list:
        if i > number_to_compare:
            number_to_compare = i
    return (number_to_compare)
