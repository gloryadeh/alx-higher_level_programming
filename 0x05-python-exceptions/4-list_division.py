#!/usr/bin/python3
def list_division(my_list, my_list2, list_length):
    i = 0
    newlist = [0 for i in range(list_length)]
    while i < list_length:
        try:
            newlist[i] = my_list[i] / my_list2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            i += 1
    return newlist
