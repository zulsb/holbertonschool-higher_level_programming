#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nl = []
    r = 0
    for e in range(list_length):
        try:
            r = my_list_1[e]/my_list_2[e]
        except TypeError:
            print("wrong type")
            r = 0
        except ZeroDivisionError:
            print("division by 0")
            r = 0
        except Exception:
            print("out of range")
            r = 0
        finally:
            nl.append(r)
    return nl
