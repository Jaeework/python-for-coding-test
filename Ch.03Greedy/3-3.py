# 숫자 카드 게임
# 각 행마다 가장 작은 수를 구한 뒤에 그 수 중에서 가장 큰 수

# my answer
n, m = map(int, input().split()) # n은 행, m은 열
result = 0
for i in range(n):
    min_value = min(list(map(int, input().split())))
    result = max(min_value, result)

print(result)


# solution 01
# min(), max() 함수 이용
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# solution 02
# 2중 반복문 사용
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)

print(result)