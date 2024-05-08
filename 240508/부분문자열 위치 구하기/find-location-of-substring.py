a = input()
b = input()

index = -1
if a == b:
    print(index+1)
else:
    for i in range(len(a)-1):
        # if len(b) == 1 and a[i+1] == b[1]:
        #     index = i+1
        #     break
        # if a[i] == b[0] and a[i+1] == b[1]:
        #     index = i
        #     break
        if a[i+1] == b[0] and len(b) == 1:
            index = i+1
            break
        for j in range(i,len(b)):

            if a[i] == b[j]:
                # index = j+1
                continue
            else:
                index = j+1
            if a[i+1] == b[j]:
                index = i+1
    print(index)