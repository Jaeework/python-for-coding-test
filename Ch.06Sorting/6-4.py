"""
    퀵 정렬 : 가장 많이 사용되는 알고리즘
             기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 교환, 그 후 리스트를 반으로 나누는 방식
             교환하기 위한 기준을 '피벗(Pivot)'이라 표현
             피벗을 설정하고 리스트를 분할하는 방법에 따라 구분
             ex) 호어 분할(Hoare Partition) : 리스트에서 첫 번째 데이터를 피벗으로 정함
             왼쪽에서부터 피벗보다 큰 데이터 탐색. 오른쪽에서부터 피벗보다 작은 데이터 탐색. 교환. 엇갈릴 경우는 피벗과 교환.
             시간복잡도 : O(NlogN) but 최악의 경우(이미 데이터가 정렬되어 있는 경우)에는 O(N^2)까지도 갈 수 있다.
"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
