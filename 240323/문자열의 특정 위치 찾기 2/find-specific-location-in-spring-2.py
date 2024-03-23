arr = ["apple","banana","grape","blueberry","orange"]
a = input()
ans_arr = []
for elem in arr:
    if elem[3] == a or elem[4] == a:
        ans_arr.append(elem)

for row in ans_arr:
    print(row)
print(len(ans_arr))