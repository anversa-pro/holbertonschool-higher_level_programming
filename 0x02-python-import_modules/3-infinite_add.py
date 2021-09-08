#!/usr/bin/python3
def add_arg(argv):
        length = len(argv) - 1
        if length == 0:
                print("{:d}".format(length))
                return
        else:
                i = 1
                sum = 0
                while i <= length:
                        sum += int(argv[i])
                        i += 1
                print("{:d}".format(sum))

if __name__ == "__main__":
        import sys
        add_arg(sys.argv)
