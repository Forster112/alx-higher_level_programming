#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    numbers = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            numbers[i].append(True)
        else:
            numbers.append(False)
        return numbers
