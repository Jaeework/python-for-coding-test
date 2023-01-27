# 팩토리얼 예제

# my answer
def factorial(i):
    if i <= 1:
        return 1
    return factorial(i - 1) * i

print(factorial(5))

# solution 01
# 반복적 구현
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

# solution 02
# 재귀적으로 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print('반복적으로 구현 :', factorial_iterative(5))
print('재귀적으로 구현 :', factorial_recursive(5))