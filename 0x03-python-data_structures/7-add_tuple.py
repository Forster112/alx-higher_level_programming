#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a < 2) or len(tuple_b < 2):
        tuple_a + (0, 0)
        tuple_b + (0, 0)
    elif len(tuple_a > 2) or len(tuple_b > 2):
        tuple_a + (0, 0)
        tuple_b + (0, 0)
    else:
        answer = ()
        answer1 = tuple_a[0] + tuple_b[0]
        answer2 = tuple_a[1] + tuple_b[1]
        answer = answer1, answer2
        return answer
