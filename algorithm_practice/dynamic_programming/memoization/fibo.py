def fib_meno(n, cache) :
    if n < 3 :
        return 1

    if n in cache :
        return cache[n]

    cache[n] = fib_meno(n-1, cache) + fib_meno(n-2, cache)

    return cache[n]


def fib(n) :
    cache = {}
    return fib_meno(n, cache)


print(fib(10))