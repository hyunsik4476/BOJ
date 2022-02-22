N = int(input())
arr = [[0]*1001 for _ in range(1001)]
for p in range(1, N+1):
    x, y, dx, dy = map(int, input().split())
    for j in range(y, y+dy):
        arr[j][x: x+dx] = [p]*dx


for p in range(1, N+1):
    ans = 0
    for y in range(1001):
        ans += arr[y].count(p)
    print(ans)