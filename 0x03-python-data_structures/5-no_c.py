#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    c = ord("c")
    C = ord("C")
    for s in my_string:
        if ord(s) != c and ord(s) != C:
            new_string += s
    return new_string
