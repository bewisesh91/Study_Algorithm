def max_product(left_cards, right_cards) :
    max_num = 0
    for left in left_cards :
        for right in right_cards :
            if max_num < left * right :
                max_num = left * right
    return max_num



left_cards = [3, 5, 7, 9, 11]
right_cards = [1, 3, 5, 7, 9]

print(max_product(left_cards, right_cards))