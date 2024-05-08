a = input()
b = input()

index = -1
if a == b:
    print(index+1)
else:
    for i in range(len(a)-1):
        
        for j in range(len(b)-1):
            if a[i] == b[j] and a[i+1] == b[j+1]:
                index = i
                break
    
    print(index)