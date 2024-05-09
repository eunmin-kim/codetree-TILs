target = input()
search = input()
index = -1
for i in range(len(target)):
    is_matched = False
    for j in range(len(search)):
        if target[i] == search[0] and target[i+1] == search[1]:
            is_matched = True
            index = i
            break
    if is_matched == True:
        print(index)
        exit()
print(index)