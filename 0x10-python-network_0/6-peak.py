#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers.
    A Maximum is a peak.
"""


def find_peak(list_of_integers):
""" retuns a peak number from a unsorted list"""

    if list_of_integers is None or len(list_of_integers) < 1:
        return None
    maximum = max(list_of_integers)
    return maximum
