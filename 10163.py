N = int(input())
cnt = [0]*(N+1)
arr = [[0]*1001 for _ in range(1001)]
for i in range(1, N+1):
    x, y, dx, dy = map(int, input().split())
    for j in range(y, y+dy):
        for k in range(x, x+dx):
            if arr[j][k] != 0:
                cnt[arr[j][k]] -= 1
                arr[j][k] = i
                cnt[i] += 1
            else:
                arr[j][k] = i
                cnt[i] += 1

for p in range(1, N+1):
    print(cnt[p])