#!/usr/bin/python3
def print_arg(argv):
    length = len(argv) - 1
    if length == 0:
        print("{:d} arguments.".format(length))
        return
    else:
        i = 1
        if length == 1:
            print("{:d} argument:".format(length))
            print("1: {:s}".format(argv[i]))
        else:
            print("{:d} arguments:".format(length))
            while i <= length:
                print("{:d}: {:s}".format(i, argv[i]))
                i += 1

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
