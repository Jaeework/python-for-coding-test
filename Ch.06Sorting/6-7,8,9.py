# 파이썬 기본 정렬 라이브러리 사용
"""
    sorted() 함수 : 퀵 정렬과 동작 방식이 비슷한 병합 정렬 사용. (정확히는 병합 정렬과 삽입 정렬을 더한 하이브리드 방식)
    최악의 경우에도 시간복잡도 O(NlogN) 보장
    sort() 함수 : 별도의 변수 선언 없이 해당 리스트의 내부 원소를 바로 정렬할 수 있다.
"""

# 6-7 sorted() 함수 사용
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

# 6-8 sort() 함수 사용
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)

# 6-9
# key 값으로 하나의 함수를 받아 정렬 기준으로 세울 수 있다.
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result) # [('바나나', 2), ('당근', 3), ('사과', 5)] 각 data의 인덱스 1 값을 기준으로 정렬