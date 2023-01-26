# 게임 개발
# n * m 크기의 직사각형, 육지 또는 바다

# solution
n, m = map(int, input().split())

# 방문한 위치 저장
d = [[0] * m for _ in range(n)]
# -> 리스트 컴프리헨션 (리스트 초기화 방법), n * m 사이즈의 2차원 배열 초기화
x, y, direction = map(int, input().split())
d[x][y] = 1

# 전체 맵 정보 저장
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0] # 북쪽으로부터
dy = [0, 1, 0, -1] # 서쪽으로부터

# 왼쪽 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# simulation 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 가 본 칸이거나 바다인 경우
    else:
        turn_time += 1

    # 네 면 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
