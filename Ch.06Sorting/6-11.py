# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름 출력

# my answer
import sys

n = int(sys.stdin.readline())

array = []

for i in range(n):
    temp = list(sys.stdin.readline().split())

    array.append((temp[0], int(temp[1])))

def setting(data):
    return data[1]

array = sorted(array, key=setting)
for i in range(len(array)):
    print(array[i][0], end=' ')


# solution 01
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')