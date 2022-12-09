#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    x = 0
    y = 0

    for tup in my_list:
        num += tup[0] * tup[1]
        den += tup[1]

    return (x / y)
