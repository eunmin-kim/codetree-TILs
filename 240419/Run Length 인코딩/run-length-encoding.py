word = input()

tmp = word[0]

word_ans = []
num_ans = []

cnt = 0

word_ans.append(word[0])
for item in word:
    if item == tmp:
        cnt += 1
    if item != tmp:
        tmp = item
        num_ans.append(cnt)
        cnt = 1
        word_ans.append(tmp)

num_ans.append(cnt)


# print(f"{len(word_ans)} {len(num_ans)}")
# print(f"{word_ans[1]} {num_ans[1]}")
print(f"{len(word_ans)+len(num_ans)}")
for i in range(len(word_ans)):

    print(f"{word_ans[i]}{num_ans[i]}",end="")