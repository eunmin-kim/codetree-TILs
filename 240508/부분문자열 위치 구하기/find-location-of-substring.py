a = input()
b = input()

index = -1
if a == b:
    print(index+1)
else:
    for i in range(len(a)-1):
        if len(b) == 1 and a[i+1] == b[0]:
            index = i+1
            break
        if a[i] == b[0] and a[i+1] == b[1]:
            index = i
            break
    print(index)