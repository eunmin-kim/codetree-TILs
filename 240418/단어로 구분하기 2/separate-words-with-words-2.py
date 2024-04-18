words = list(map(str,input().split()))

for i in range(1,len(words)+1,2):
    print(f"{words[i-1]}")