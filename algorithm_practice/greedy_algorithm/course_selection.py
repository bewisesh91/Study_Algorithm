def course_selection(course_list) :
    result = []

    sorted_course_list = sorted(course_list, key=lambda x : (x[1], x[0]))
    for course in sorted_course_list :
        if len(result) == 0 :
            result.append(course)
        else :
            if result[-1][1] > course[0] :
                pass
            else :
                result.append(course)
    
    return result

print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))

