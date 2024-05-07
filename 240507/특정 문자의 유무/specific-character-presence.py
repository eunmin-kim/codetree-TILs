a = input()
b = "ee"
c = "ab"
exists = "No"
all_same = "No"
for i in range(len(a)-1):

    if a[i] == b[0] and a[i+1] == b[1]:
        exists = "Yes"
    if a[i] == c[0] and a[i+1] == c[1]:
        all_same = "No"

print(f"{exists} {all_same}")