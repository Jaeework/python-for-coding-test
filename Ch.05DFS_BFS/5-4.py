# 재귀 함수의 종료 조건
# 재귀 함수를 100 번만 호출하도록
# 재귀 함수는 내부적으로 스택 자료구조와 동일하다.

def recursive_function(i):
    if i == 100:
        return
    print(i, '번쨰 재귀 함수에서', i + 1 , '번째 재귀 함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)

