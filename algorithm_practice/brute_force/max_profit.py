def max_profit(profits) : 
    max_profit_dict = {}

    for i in range(len(profits)) :
        profit = 0

        for j in range(i, len(profits)) :
            temp = profit + profits[j]
            
            if temp > profits[j] :
                max_profit_dict[temp] = [i, j]
            
            profit += profits[j]
    
    max_profit = sorted(max_profit_dict, reverse = True)[0]

    return max_profit, max_profit_dict[max_profit]


ex_profits = [1, 0, -3, 5, 8, 9, 11, -3, -8, 15]
print(max_profit(ex_profits))