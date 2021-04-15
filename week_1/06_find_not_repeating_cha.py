input = "adfasdfasdfasdfsdfasdfe"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요!

    space = []
    removed = []
    for i in string:
        if i in space:
            space.remove(i)
            removed.append(i)
        else :
            space.append(i)

    for i in removed :
        if i in space :
            space.remove(i)

    return space


result = find_not_repeating_character(input)
print(result)