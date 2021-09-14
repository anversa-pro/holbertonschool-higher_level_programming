#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for list_j, i in enumerate(my_list):
        if i % 2 == 0:
            new_list[list_j] = True
        else:
            new_list[list_j] = False
    return(new_list)
