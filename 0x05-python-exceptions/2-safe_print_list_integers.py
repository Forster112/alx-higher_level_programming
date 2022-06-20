#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        print("{:d}".format(*my_list[:x], sep=""), end="")
        print()
        counter = 0
        for i in my_list[:x]:
            counter += 1
        return counter
    except ValueError:
        return counter
