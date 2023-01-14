# Greedy : 현재 상황에서 지금 당장 좋은 것만 고르는 방법
# '가장 큰 순서대로', '가장 작은 순서대로' 와 같이 문제에서 기준을 제시.

"""
 거스름돈으로 사용할 500원, 100원, 50원, 10원
 손님에게 거슬러 줘야 할 돈 N원
 거슬러 줘야 할 동전의 최소 개수는? (단, 돈 N의 개수는 항상 10의 배수)
"""

# 거스름돈 액수
import time

n = 1260

count = 0

coin_types = [500, 100, 50, 10]

start_time = time.time()
for i in coin_types:
    count += n // i
    if(n % i == 0):
        break
    else:
        n = n % i

end_time = time.time()
print("time:", end_time - start_time)

print(count)