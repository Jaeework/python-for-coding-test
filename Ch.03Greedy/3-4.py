# 어떠한 수 n이 1이 될 때까지 두 과정 중 하나를 반복적으로 수행. n이 1이 되는 최소 횟수
# 1. N에서 1 빼기
# 2. N을 K로 나누기
# 2번 연산은 n이 k로 나누어 떨어질 때만 가능

# my answer
n, k = map(int, input().split())
cnt = 0
while True :
    if n == 1:
        break

    if(n % k == 0):
        n = n / k
    else:
        n = n - 1
    cnt += 1

print(cnt)

# solution 01
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1

    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)


# solution 02
# n이 k의 배수가 되도록 한 번에 빼기
n, k = map(int, input().split())
result = 0

while True:
    # (n == k로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n 이 k 보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

    # 마지막 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

# solution 02 응용
# n이 k의 배수가 되도록 한 번에 빼기
n, k = map(int, input().split())
result = 0

while True:
    # (n == k로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    remainder = n % k
    result += remainder
    n = n - remainder
    # n 이 k 보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

    # 마지막 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

