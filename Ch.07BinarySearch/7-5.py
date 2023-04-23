# my answer
import sys

n = int(sys.stdin.readline().rstrip())
stockList = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
orderList = list(map(int, sys.stdin.readline().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for i in orderList:
    result = binary_search(stockList, i, 0, n - 1)
    if result == None:
        print("No", end=" ")
    else:
        print("Yes", end=" ")


# solution 01

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

n = int(input()) # 가게의 부품개수 n
array = list(map(int, input().split())) # 가게에 있는 전체 부품 번호
array.sort() # 이진탐색은 데이터 정렬을 전제조건으로 함. 빼먹지 말기!!!!!
m = int(input()) # 손님이 요청한 부품 개수 m
x = list(map(int, input().split())) # 손님이 요청한 부품 번호

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')