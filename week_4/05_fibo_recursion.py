input = 20


def fibo_recursion(n):
    # 구현해보세요!
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765

# 문제는 input의 숫자가 커지면 recursivi한 경우 속도가 너무 느려진다.
# why? 계산했던 것을 여러 번 반복하기 때문