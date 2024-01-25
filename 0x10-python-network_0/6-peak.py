#!/usr/bin/python3
""" function for finding a peak on a list """


def find_peak(list_of_integers):
    """
    function finds the peak of a list while having the lowerst time complexity

    Keyword arguments: list_of_integers
    argument -- a list of integers
    Return: returns the peak of teh list provided
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
