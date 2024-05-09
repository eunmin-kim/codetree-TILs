a, b = map(str,input().split())
b = list(b)

ab = a[:2]

for i in range(2):
    b[i] = ab[i]

c = ''.join(b)

print(c)