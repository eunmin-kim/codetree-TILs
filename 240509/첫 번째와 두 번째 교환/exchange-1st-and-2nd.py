a = input()
d = list(a)
first_char = d[0]
second_char = d[1]

# 모든 문자에 대해 반복
for i in range(len(d)):
    if d[i] == first_char:
        d[i] = second_char
    elif d[i] == second_char:
        d[i] = first_char

# 결과 문자열 생성
c = ''.join(d)
print(c)