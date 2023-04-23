"""
    파라메트릭 서치 : Parametric Search. 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 사용
    적절한 답을 찾을 때까지 조건의 만족 여부('yes' or 'no')에 따라서 탐색 범위를 좁혀나간다. 주로 이진탐색 사용
"""

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for i in array:
        if i > mid:
            total += i - mid

    if total < m:
        end = mid - 1
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 여기서 기록
        start = mid + 1

print(result)
