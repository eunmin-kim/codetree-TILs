a = input()
a = list(a)
tmp = a[0]
tmp2 = a[1]

for i in range(len(a)):
    if a[i] == tmp:
        a[i] = tmp2
        continue
    elif a[i] == tmp2:
        a[i] == tmp
        continue

c = ''.join(a)
print(c)