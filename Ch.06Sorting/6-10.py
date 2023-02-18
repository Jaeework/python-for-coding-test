# 수열을 내림차순으로 정렬

# my answer
import sys

n = int(sys.stdin.readline())

array = []

for i in range(n):
    array.append(int(sys.stdin.readline()))

array.sort(reverse=True)
print(array)


# solution 01
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')