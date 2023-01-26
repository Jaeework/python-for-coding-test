# 왕실의 나이트

# solution
# x : +- 2 -> y : +-1
# x : +- 1 -> y : +-2

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
"""
ord(문자) : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환
ex) ord('a') = 97
cf) chr(정수) : 하나의 정수를 인자로 받아 해당하는 유니코드 문자를 반환
    chr(97) = 'a'
"""

steps = [(-2, -1), (2, -1), (-2, 1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = row + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)




