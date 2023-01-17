# 구현(Implementation) : 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
# 완전 탐색 : 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
# 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 문제 유형

# 상하좌우

# my answer
n = int(input())
plans = list(input().split())
x, y = 1, 1

# r l u d
# *X, Y축 헷갈리지 말기*
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
move_type = ['R', 'L', 'U', 'D']

for plan in plans:
    for i in range(len(move_type)):
        if move_type[i] == plan:
            nx = x + dx[i]
            ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        else:
            x = nx
            y = ny

print(x, y)


#solution
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
