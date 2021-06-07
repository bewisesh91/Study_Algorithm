def flip(some_list) :
    if len(some_list) == 0 or len(some_list) == 1 :
        return some_list
    else :
        return some_list[-1:] + flip(some_list[:-1])

ex_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(flip(ex_list))