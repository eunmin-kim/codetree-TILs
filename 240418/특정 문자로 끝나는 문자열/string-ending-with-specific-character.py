words_arr = []
for i in range(10):
    word = input()
    words_arr.append(word)

x = input()

ans = []
for word in words_arr:
    if word[len(word)-1] == x:
        ans.append(word)

if len(ans) == 0:
    print("None")

for item in ans:
    print(item)