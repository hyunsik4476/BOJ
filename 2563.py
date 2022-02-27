N = int(input())
arr = [[0]*100 for _ in range(100)]
for i in range(N):
    stx, sty = map(int, input().split())
    for y in range(10):
        for x in range(10):
            if 100>stx+x>=0 and 100>sty+y>=0:
                arr[sty+y][stx+x] = 1
ans = 0
for j in range(100):
    ans += arr[j].count(1)
print(ans)