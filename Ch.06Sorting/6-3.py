"""
    삽입 정렬 : 특정한 데이터를 적절한 위치에 '삽입'하여 정렬
               필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬되어 있을 때' 훨씬 효율적
               데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정.
               첫 데이터는 그 자체로 정렬되어 있다고 가정하기 때문에 두 번째 데이터부터 시작
               시간 복잡도 : O(N^2) 이나 거의 정렬되어 있는 최선의 경우에는 O(N)으로 다른 정렬 알고리즘보다 효율적일 수 있다.
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):   # 인덱스 i부터 1까지 감소하며 반복하는 문법 range(start, end + 1, step)
        if array[j] < array [j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)

