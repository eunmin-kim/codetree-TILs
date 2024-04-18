n = int(input())

words_arr = []
for i in range(n):
    item = input()
    words_arr.append(item)
x = input()
cnt = 0
word_len = 0

for i in words_arr:
    if i[0] == x:
        cnt += 1
        word_len += len(i)

avg = round(word_len / cnt,3)
print(f"{cnt} {avg:.2f}")