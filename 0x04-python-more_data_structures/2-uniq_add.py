#!/bin/usr/python3
def uniq_add(my_list=[]):
    result = 0
    if my_list is None:
        return (result)
    for i in set(my_list):
        result += i
    return(result)
