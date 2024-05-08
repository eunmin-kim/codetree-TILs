a, b = map(str, input().split())

index = -1
for i in range(len(a)-1):
    if a[i] == b:
        index = i
        break
if index == -1:
    print("No")
else:
    print(index)