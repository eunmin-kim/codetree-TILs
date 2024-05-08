a = input()

b = 'ee'
c = 'eb'

b_cnt = 0
c_cnt = 0
for i in range(len(a)-1):
    if a[i] == b[0] and a[i+1] == b[1]:
        b_cnt += 1
    if a[i] == c[0] and a[i+1] == c[1]:
        c_cnt += 1


print(f"{b_cnt} {c_cnt}")