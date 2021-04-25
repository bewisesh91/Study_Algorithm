input = "abcabcabcabcdededededede"
# 반복은 언제까지가 유효할 것인가?
# input의 반까지만 유효하고 그 이상은 의미가 없다.

def string_compression(string):
    n = len(string)
    result = []
    for split_size in range(1, n//2 + 1) :
        splited = []
        for i in range(0, n, split_size) :
            splited.append(string[i : i + split_size])

        count = 1
        count_dict = {}
        count_dict[1] = []
        for i in range(len(splited)-1) :
            if splited[i] == splited[i+1] :
                count += 1
                count_dict[splited[i]] = count
            else :
                if splited[i] not in count_dict :
                    count_dict[1].append(splited[i])
                count = 1
        if splited[-1] not in count_dict :
            count_dict[1].append(splited[-1])

        string_count = ""
        for key, value in count_dict.items() :
            if key == 1 :
                for i in count_dict[1]:
                    string_count += i
            else :
                string_count = string_count + str(value) + key
        result.append(len(string_count))

    return min(result)


print(string_compression(input))  # 14 가 출력되어야 합니다!