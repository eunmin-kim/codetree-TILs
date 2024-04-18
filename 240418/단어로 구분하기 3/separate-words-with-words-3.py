words = list(map(str, input().split()))

for i in range(len(words)-1,-1,-1):
    print(f"{words[i]}")