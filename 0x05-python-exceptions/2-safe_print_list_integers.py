#!/usr/bin/python3y
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    printed = 0
    try:
        for i in my_list[:x]:
            if isinstance(i, int):
                print("{:d}".format(i), end="")
                printed += 1
        print()
    except:
        continue
    return(printed)
