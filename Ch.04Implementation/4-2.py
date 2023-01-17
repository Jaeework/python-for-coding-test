# 시각
# 00시 00분 00초부터 n시 59분 59초까지의 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수
# 완전 탐색 유형

# my answer
n = int(input())
cnt = 0

for i in range(n + 1):

    for j in range(60):
        for k in range(60):
            if not(str(k).find('3') == -1 and str(j).find('3') == -1 and str(i).find('3') == -1):
                cnt += 1


print(cnt)

# solution
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)