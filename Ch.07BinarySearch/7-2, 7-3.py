'''
    이진 탐색 : 반으로 쪼개면서 탐색
    시작점, 끝점, 중간점
    중간점과 찾으려는 데이터를 반복적으로 비교해서 탐색
    배열 내부의 데이터가 정렬되어 있어야만 사용 가능.
    한 번 확인할 때마다 확인하는 원소 개수가 절반씩 줄어듬. 시간복잡도 O(logN)
'''

# 재귀함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

# 원소의 개수와 찾고자 하는 문자열
n, target = list(map(int, input().split()))
# 전체 원소
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)




# 재귀함수 사용 없이 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


# 원소의 개수와 찾고자 하는 문자열
n, target = list(map(int, input().split()))
# 전체 원소
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)