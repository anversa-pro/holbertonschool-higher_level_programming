#!/usr/bin/python3
def print_arg(argv):
    length = len(argv) - 1
    if length == 0:
        print("{:d} argument.".format(length))
        return
    else:
        if length == 1:
            print("{:d} argument:".format(length))
        else:
            print("{:d} arguments:".format(length))
            i = 1
            while i <= length:
                print("{:d}: {:s}".format(i, argv[i]))
                i += 1

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
