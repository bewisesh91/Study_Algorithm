from collections import deque

balanced_parentheses_string = "()))((()"


def is_correct_parentheses(string) :
    stack = []
    for s in string :
        if s == '(' :
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0


def change_to_correct_parenthesis(string) :
    if string == "" :
        return ""

    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue :
        char = queue.popleft()
        u += char
        if char == "(" :
            left += 1
        else :
            right += 1
        if left == right :  # u는 더 이상 균형잡힌 괄호 문자열로 분리되면 안되기 때문에 첫 번째 조건 충족할 때 멈춰 준다.
            break
    v = ''.join(list(queue))

    if is_correct_parentheses(u) :
        return u + change_to_correct_parenthesis(v)
    else :
        reversed_string = ""
        for char in u[1:-1] :
            if char == "(" :
                reversed_string += ")"
            else :
                reversed_string += "("
        return "(" + change_to_correct_parenthesis(v) + ")" + reversed_string



def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string) :
        return balanced_parentheses_string
    else :
        return change_to_correct_parenthesis(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!