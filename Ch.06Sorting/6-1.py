"""
 정렬 : 데이터를 특정한 기준에 따라 순서대로 나열하는 것
 주요 종류 : 선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬

 선택 정렬 : 가장 작은 데이터를 선택해 맨 앞 데이터와 바꾸고, 그다음 작은 데이터를 앞에서 두 번째 데이터와 바꾸는 과정을 반복 수행
            시간복잡도 : O(N^2). 다른 정렬 알고리즘에 비교했을 때 매우 비효율적이다.
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)