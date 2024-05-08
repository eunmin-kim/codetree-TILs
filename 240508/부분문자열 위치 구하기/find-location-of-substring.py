a = input()
b = input()

index = -1
for i in range(len(a)-1):
    if a[i] == b[0] and a[i+1] == b[1]:
        index = i

print(index)