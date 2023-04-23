# 7-5를 계수정렬 사용하여 풀기
# 모든 원소의 번호를 포함할 수 있는 크기의 리스트를 만든 뒤, 인덱스에 직접 접근하여 확인

n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')



# 집합 자료형 이용한 solution
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')