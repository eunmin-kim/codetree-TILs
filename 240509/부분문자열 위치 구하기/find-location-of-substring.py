import sys
target = input()
search = input()
index = -1
for i in range(len(target)):

    is_matched = True

    if i + len(search) - 1 >= len(target):
        continue
    for j in range(len(search)):
        if target[i+j] != search[j]:
            is_matched = False
    
    if is_matched == True:
        print(i)
        sys.exit()
print(index)