#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print(*my_list[:x], sep="", end="")
        print()
        return my_list[x - 1]
    except IndexError:
        return my_list[-1]
