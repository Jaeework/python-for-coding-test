"""
    다익스트라(Dijkstra, 데이크스트라) : 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘.
    음의 간선이 없을 때 정상적으로 동작. 음의 간선이란 0보다 작은 값을 가지는 간선
    일종의 그리디 알고리즘
    1. 출발 노드 설정
    2. 최단 거리 테이블(1차원 리스트) 초기화
    3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
    4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
    5. 과정 3, 4를 반복
    매번 현재 처리하고 있는 노드를 기준으로 주변 간선 확인
    O(V^2)의 시간복잡도. V는 노드의 수
"""


import sys
input = sys.stdin.readline
INF = int(1e9)  # 초기상태에서는 다른 모든 노드로 가는 최단 거리를 '무한'으로 초기화. 10억.

n, m = map(int, input().split())    # n : 노드의 개수, m : 간선의 개수
start = int(input())
graph = [[] for i in range(n + 1)]  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False] * (n + 1)
distance = [INF] * (n + 1)  # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a 노드에서 b 노드로 가는 비용이 c

# 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드 번호
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 # 시작노드 본인으로부터 본인까지의 거리이므로 0으로 초기화
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        # 최단 거리 가장 짧은 노드를 꺼내 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 가는게 더 짧을 경우에만 distance 갱신
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])