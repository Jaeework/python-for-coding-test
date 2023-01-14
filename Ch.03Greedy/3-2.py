# 큰 수의 법칙
# 다양한 수로 이루어진 배열이 있을 때 주어진 수를 M번 더하여 가장 큰 수를 만드는 법칙. 단, 한 인덱스는 연속으로 K번만 더할 수 있다.
# 배열의 크기 N

# my answer
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

result = 0
for i in range (m):
    if(i % k == 0 and i != 0):
        result += data[n-2]
    else:
        result += data[n-1]
print(result)


# solution 01 => m 의 크기가 100 억 이상으로 커지면 시간 초과 판정
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0 :
            break
        result += first
        m -= 1
    if m == 0 :
        break
    result += second
    m -= 1

print(result)

# solution 02
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수
count = int(m / (k + 1)) * k + (m % (k + 1))

result = 0
result += first * count
result += second * (m - count)

print(result)