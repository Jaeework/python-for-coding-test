# 음료수 얼려 먹기
# n * m 크기의 얼음틀. 0은 아이스크림 1은 칸막이

# my answer
import sys

n, m = map(int, sys.stdin.readline().split())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def icecream(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 1:
        return False
    # visited 체크
    graph[x][y] = 1
    icecream(x - 1, y)
    icecream(x, y - 1)
    icecream(x + 1, y)
    icecream(x, y + 1)
    return True

result = 0
for i in range(n):
    for j in range(m):
        if icecream(i, j) == True:
            result += 1

print(result)

# solution 01
n, m = map(int, input().split())

# 2차원 리스트 맵 정보 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정 노드 방문 뒤, 연결된 모든 노드들도 함께 방문
def dfs(x, y):
    # 주어진 범위 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드 아직 방문 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상,하,좌,우 모두 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)