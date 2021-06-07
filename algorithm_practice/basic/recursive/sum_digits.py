def sum_digits(n):
    if n < 10 :
        return n
    else :
        str_n = str(n)
        return int(str_n[-1]) + sum_digits(int(str_n[:-1]))


print(sum_digits(10))
print(sum_digits(11))
print(sum_digits(12))