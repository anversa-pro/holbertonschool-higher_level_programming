#r/bin/python3y
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        for i in my_list[:x]:
            if isinstance(i, int):
                print("{}".format(i), end="")
        print()
    except:
        return(i)
    return(i)
