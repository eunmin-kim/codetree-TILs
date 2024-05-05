a = input()

# for i in range(len(a)-1,-1,-2):
#     print(f"{a[i]}",end="")
ans = []

for i in range(1,len(a)+1,1):
    if i % 2 == 0:
        ans.append(a[i-1])

for i in range(len(ans)-1,-1,-1):
    print(f"{ans[i]}")