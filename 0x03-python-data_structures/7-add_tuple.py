#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a < 2 or tuple_b < 2:
        tuple_a.append(0)
        tuple_b.append(0)
    elif tuple_a > 2 or tuple_b > 2:
        tuple_a = (0, 0)
        tuple_b = (0, 0)
    else:
        answer1 = tuple_a[0] + tuple_b[0]
        answer2 = tuple_a[1] + tuple_b[1]
        answer = (answer1, answer2)
        return answer
