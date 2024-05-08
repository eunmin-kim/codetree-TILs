a = input()
b = input()

index = -1
if a == b:
    print(index+1)
else:
    for i in range(len(a)-1):
        is_match = False
        for j in range(len(b)-1):
            if a[i] == b[j] and a[i+1] == b[j+1]:
                is_match = True
        if is_match == True:
            index = i
            break
print(index)