def min_coin_count(value, coin_list) :
    count = 0

    for coin in sorted(coin_list, reverse=True):
        temp = value // coin
        count += temp    
        value = value - (coin * temp)

    return count

default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))

