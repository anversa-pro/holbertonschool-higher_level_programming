#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_keys = {}
    for i in sorted(a_dictionary):
        ordered_keys[i] = a_dictionary[i]
        print("{}:{}".format(i, ordered_keys[i]))
