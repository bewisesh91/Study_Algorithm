def flip(list) :
    if len(list) < 2 :
        return list
    else :
        return list[-1:] + flip(list[:-1])

ex_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(flip(ex_list))


