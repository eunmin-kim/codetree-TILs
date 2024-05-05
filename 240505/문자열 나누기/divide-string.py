n = int(input())

strs = list(map(str,input()))

a = ""
# print(strs)
for i in strs:
    for j in i:
        if j != " ":
            a += j
# print(a)
cnt = 0
for j in range(len(a)):
    if j % 5 == 0 and j is not 0:
        print()
    print(f"{a[j]}",end="")