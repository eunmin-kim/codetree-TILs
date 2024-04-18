n = int(input())
cnt = 0
words_len = 0
for i in range(n):
    words = input()
    for i in range(len(words)):
        if i == 0 and words[i] == "a":
            cnt += 1
    words_len += len(words)

print(f"{words_len} {cnt}")