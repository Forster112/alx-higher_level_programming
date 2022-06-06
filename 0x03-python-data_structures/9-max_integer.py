#!/usr/bin/python3

def max_integer(my_list=[]):
    max_num = my_list[0]
    for i in my_list:
        if len(my_list) == 0:
            return "None"
        elif i > max_num:
            max_num = i
            return max_num
