a = input()
l_a = list(a)
l_a[1] = 'a'
l_a[len(a)-2] = 'a'
b = ''.join(l_a)
print(b)