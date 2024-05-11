a = input()
b = list(a)
str_a1 = b[0]
str_a2 = b[1]
for i in range(len(b)):
    if b[i] == str_a2:
        b[i] = str_a1


b= ''.join(b)

for i in b:
    print(i,end="")