arr = []
for i in range(3):
    input_s = input()
    ans = len(input_s)
    arr.append(ans)
print(f"{max(arr)- min(arr)}")