x = int(input())

# 계산 결과 저장 위한 DP 테이블 초기화
d = [0] * 30001

# Bottom-up
for i in range(2, x + 1):
    #1을 빼는 경우
    d[i] = d[i - 1] + 1
    #2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])