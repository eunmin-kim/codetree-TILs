n,m = map(int, input().split())

placed = [
    [0 for _ in range(n)]
    for _ in range(n)
]
for i in range(m):
    a,b = tuple(map(int, input().split()))
    placed[a-1][b-1] = a * b

for r in placed:
    for c in r:
        print(c,end=" ")
    print()