"""
    다이나믹 프로그래밍
    메모리 공간을 약간 더 사용하여 연산 속도를 비약적으로 증가시킬 수 있는 방법 중 하나
    동적 계획법이라고도 한다.
    대표예시 : 피보나치 수열
"""

# my answer
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)

print(fibo(100))

# 재귀 함수 사용시 n이 커질수록 수행 시간이 기하급수적으로 늘어남. 같은 함수를 여러 번 호출하기 때문. => O(2^n)
# 메모이제이션(Memoization) 기법을 사용하여 해결
# 탑다운(Top-down) 방식이라고 불리움
# 한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법. (=캐싱Caching)
# 시간복잡도 O(N)

#메모이제이션 하기 위한 리스트 초기화
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1

    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산한 적 없는 문제라면 점화식에 따라 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))


# 어떤 함수가 호출되었는지 확인
d = [0] * 100

def fibo(x):
    print('f(' + str(x) + ')', end=' ')

    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

fibo(6)


# 보텀업(Bottom-up) 방식 : 단순 반복문을 이용하여 작성

# DP 테이블 초기화
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])