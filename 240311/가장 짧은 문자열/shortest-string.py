max_n = -1
min_n = 21
for i in range(3):
    input_s = input()
    ans = len(input_s)
    if max_n < ans:
        max_n = ans
    elif min_n > ans and max_n != ans:
        min_n = ans
print(f"{abs(max_n - min_n)}")