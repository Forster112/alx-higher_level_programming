#!/usr/bin/python3

def max_integer(my_list=[]):
    max_num = my_list[0]
    if len(my_list) == 0:
        return "None"
    for i in range(my_list):
        if my_list[i] > max_num:
            max_num = my_list[i]
        return max_num
