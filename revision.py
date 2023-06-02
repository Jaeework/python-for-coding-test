# 3 Greedy
# 3-1
import sys
n = int(sys.stdin.readline())

coin_types = [500, 100, 50, 10]
result = 0

for coin in coin_types:
    result += n // coin
    n %= coin

    if n == 0:
        break

print(result)


# 3-2
import sys
n, m, k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

array.sort()
first = array[n - 1]
second = array[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        else:
            result += first
            m -= 1

    if m == 0:
        break
    else:
        result += second
        m -= 1

print(result)


# 3-2
"""
    k = 3, 가장 큰 수 6, 그 다음 큰 수 5로 가정했을 때
    6 6 6 5 가 계속적으로 반복
    m // (k + 1) + m % (k + 1) 를 통해 솔루션 구함
"""
import sys
n, m, k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

array.sort()
first = array[n - 1]
second = array[n - 2]

result = 0
"""
c = m // (k + 1) # 총 곱하는 횟수 => 남은 횟수 : m - (k + 1) * c

result += (first * k + second) * c + first * (m - (k + 1) * c)
"""

# 가장 큰 수 곱해지는 횟수
count = m // (k + 1) * k
count += m % (k + 1)

result += first * count + second * (m - count)

print(result)


# 3-3
import sys

n, m = map(int, sys.stdin.readline().split())
result = 0

for i in range(n):
    array = list(map(int, sys.stdin.readline().split()))
    array.sort()
    if array[0] > result:
        result = array[0]

print(result)

# 3-4
import sys
n, k = map(int, sys.stdin.readline().split())
count = 0

while True:
    if n == 1:
        break

    count += 1

    if n % k == 0:
        n //= k
    else:
        n -= 1

print(count)


# 4-1
import sys
n = int(sys.stdin.readline())
datas = list(sys.stdin.readline().split())

directions = ['L', 'R', 'U', 'D']
# X, Y 순서 헷갈리지 않기....
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
x = 1
y = 1

for data in datas:
    move = moves[directions.index(data)]
    x_after = x + move[0]
    y_after = y + move[1]
    if x_after <= n + 1 and x_after >= 1:
        x = x_after
    if y_after <= n + 1 and y_after >= 1:
        y = y_after

print(x, y)


# 4-1
import sys
n = int(sys.stdin.readline())
plans = list(sys.stdin.readline().split())

x, y = 1, 1

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    move = move_types.index(plan)
    x_after = x + dx[move]
    y_after = y + dy[move]

    if x_after < 1 or x_after > n or y_after < 1 or y_after > n:
        continue
    x = x_after
    y = y_after

print(x, y)

# 4-2
hh = int(input())

mm, ss = 60, 60
count = 0

for i in range(hh + 1):
    for j in range(mm):
        for h in range(ss):
            time = str(i) + str(j) + str(h)
            if time.find('3') != -1:
                count += 1

print(count)

# 4-3
xasis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

n = input()
x, y = int(n[1]), xasis.index(n[0]) + 1

steps = [(2, 1), (2, -1), (-2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
count = 0

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    count += 1

print(count)

# 4-4
n, m = map(int, input().split())
# a가 y, b가 x
