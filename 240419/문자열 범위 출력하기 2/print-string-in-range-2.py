word = input()
x = int(input())
cnt = 0
for i in range(len(word)-1,-1,-1):
    if cnt == x:
        break
    print(word[i],end="")
    cnt += 1