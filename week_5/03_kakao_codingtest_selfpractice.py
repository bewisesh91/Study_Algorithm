

# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
# 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.

# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.

# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.


from collections import deque


balanced_parentheses_string = "()))((()"


def is_correct_parentheses(string) :
    stack = []
    for s in string :
        if s == '(' :
            stack.append(s)
        elif stack :
            stack.pop()

    if len(stack) == 0 :
        return True
    else :
        return False


def change_to_correct_parentheses(string) :
    if string == "" :
        return ""

    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while queue :
        parentheses = queue.popleft()
        if parentheses == "(" :
            left += 1
            u += parentheses
        else :
            right += 1
            u += parentheses
        if left == right :
            break

    v = ''.join(list(queue))

    if is_correct_parentheses(u) :
        return u + change_to_correct_parentheses(v)
    else :
        reversed_u = ""
        for i in u[1:-1] :
            if i == "(" :
                reversed_u += ")"
            else :
                reversed_u += "("
        return "(" + change_to_correct_parentheses(v) + ")" + reversed_u


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string) :
        return balanced_parentheses_string
    else :
        return change_to_correct_parentheses(balanced_parentheses_string)

print(get_correct_parentheses(balanced_parentheses_string))