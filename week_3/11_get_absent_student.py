all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    # 구현해보세요!
    studet_dict = {}
    for key in all_array:
        studet_dict[key] = True

    for key in present_array:
        del studet_dict[key]

    for key in studet_dict.keys():
        return key


def get_absent_student(all_array, present_array):
    set(all_array)
    for i in present_array:
        if i in all_array :
            all_array.remove(i)
    return all_array

print(get_absent_student(all_students, present_students))